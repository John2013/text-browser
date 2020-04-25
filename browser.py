import sys
from os import mkdir
from os.path import isfile, join
from typing import List

import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

HEADER_TAGS = (f"h{number}" for number in range(1, 6 + 1))

TEXT_TAGS = ("p", *HEADER_TAGS, "a", "ul", "ol", "li")


def parse_html(raw_html: str):
    init()
    text = ""
    soup = BeautifulSoup(raw_html, 'html.parser')
    for tag in soup.select(",".join(TEXT_TAGS)):
        line = tag.get_text()
        if tag.name == "a":
            line = f"{Fore.BLUE}{line}{Style.RESET_ALL}"
        text += f"{line}\n"
    return text


def save_page(pages_dir, url, text):
    try:
        mkdir(pages_dir)
    except FileExistsError:
        pass
    name = url.rsplit(".", 1)[0]
    with open(join(pages_dir, name), 'w', encoding="UTF-8") as page_file:
        page_file.write(text)


def is_url_valid(url: str):
    return "." in url


def get_page(url: str):
    protocol = "https://"
    if not url.startswith(protocol):
        url = f"{protocol}{url}"
    result = requests.get(url)
    if result.ok:
        return parse_html(result.text)
    else:
        return False


def print_file(pages_dir: str, url: str):
    resource_name = url.rsplit(".", 1)[0]
    file_path = join(pages_dir, resource_name)
    if isfile(file_path):
        with open(file_path, 'r', encoding="UTF-8") as page_file:
            print(page_file.read())
        return True
    else:
        print("error")
        return False


pages_dir = sys.argv[1] if len(sys.argv) > 1 else "pages"
history: List[str] = []

while True:
    url = input().lower()
    if url == "exit":
        exit()
    elif url == "back":
        if len(history) > 1:
            history.pop()
            print_file(pages_dir, history[-1])
        else:
            print("")
    elif is_url_valid(url):
        page_text = get_page(url)
        save_page(pages_dir, url, page_text)
        print_file(pages_dir, url)
        history.append(url)
    else:
        print_file(pages_dir, url)
