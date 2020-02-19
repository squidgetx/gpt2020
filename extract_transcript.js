from bs4 import BeautifulSoup
import urllib.request
import fileinput
import pdb
import os

if __name__ == "__main__":
    for line in fileinput.input():
        soup = BeautifulSoup(html_doc, 'html.parser')
