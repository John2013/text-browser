# Text browser

just prints web pages as text in console

## Installation

0. Install Python3.8 or newer
1. Create a virtual environment if you want
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # if linux
    venv\Scripts\activate.bat  # if windows cmd
    venv\Scripts\Activate.ps1  # if windows PowerShell
    ```

2. Install packages

    ```bash
    pip install -r requirements
    ```

## Start

```bash
python browser.py [pages_dir]
```
`pages_dir` - dir for saving of html of web pages, default: `pages`

## Example

```
> www.motherfuckingwebsite.com
This is a motherfucking website.
Seriously, what the fuck else do you want?
You probably build websites and think your shit is special. You think your 13 megabyte parallax-ative home page is going to get you some fucking Awwward banner you can glue to the top corner of your site. You think your 40-pound jQuery file and 83 polyfills give IE7 a boner because it finally has box-shadow. Wrong, motherfucker. Let me describe your perfect-ass website:
...
```
