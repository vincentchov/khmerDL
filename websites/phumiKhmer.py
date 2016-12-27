"""
    This script is intended to parse Phumi Khmer pages.
"""
from __future__ import unicode_literals
import youtube_dl
import requests
import html
from bs4 import BeautifulSoup
import re

"""
    Returns a list of URLs to download given the URL for a show
"""

def phumiKhmerURLs(url):
    # Get the HTML page for a given show's URL
    r = requests.get(url)

    text_soup = BeautifulSoup(r.text, "html.parser")

    # Find the HTML element that contains {"file"
    files_string = text_soup.find(string=re.compile("\{\"file\""))

    # Break up that array by newlines
    files_string_list = files_string.split("\n")

    # Select only the lines that contain {"file"
    regex = re.compile(".*(file).*")
    files_string_list = [m.group(0) for l in files_string_list for m in [regex.search(l)] if m]

    return files_string_list

# Get the HTML for the Phumi Khmer page
url = 'http://www.phumikhmer9.com/2016/09/lbech-sne-meayea.html'
print(str(phumiKhmer(url)))
