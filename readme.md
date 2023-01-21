# Artix
Artix is a simple web scrapper GUI built using tkinter and uses python to load the articles from the web.

## Technologies Used 🛠️

- Tkinter -> A Python Package used for building GUIs.
- Customtkinter -> A custom version of tkinter used for building beautiful GUIs.
- Requests -> A Python Package used for sending HTTP requests.
- BeautifulSoup -> A Python Library used for web scraping by parsing the HTML or XML documents.

## How it works ?

- Firstly the request package is used to make HTTP requests with the website and it returns the HTML Document.
- BeautifulSoup takes that HTML document and parses it using an HTML parses.
- BeautifulSoup is used to find the relevant tags that are used by the websites to host the content e.g Header Tags, Paragraph Tags etc
- Finally the parsed text is then displayed in the customtkinter's article box for a viewer to view.

## How to use it ?

1. Install Requests, BeautifulSoup, TKinter and customtkinter on your device by running command `pip install requests bsf tkinter customtkinter` or `python3 -m pip install requests bsf tkinter customtkinter`. You must have python installed. If not visit [Python.org's website](https://python.org).
2. Simply open an IDE or terminal and run the file by using the command `python Artix.py` or `python3 Artix.py`.
3. Enjoy!

## CLI Version

I have also created an CLI version of this which doesn't have any GUI. You can find that by [clicking here](https://github.com/thatsmanmeet/Python-Codes/blob/main/programs/articlescraper.py).

## Disclaimer

Web Scraping may or may not be **illegal** based on the copyright laws and hence it is advised to used this tool wisely. This tool is solely made for educational purposes and the developer takes no responsibility on how you use it.