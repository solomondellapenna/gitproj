import requests
from bs4 import BeautifulSoup
import sys
import re

def id_names(list_of_ids):
    file_name = input("Page Title: ") + ".txt"
    all_text = list()
    for number in list_of_ids:
        ids = (input(number + " Id: "))
        id_text = re.sub(r" ?\[[^]]+\] | ?\([^)]+\)","",(BeautifulSoup((requests.get("https://simple.wikipedia.org/wiki/" + ids)).content, 'html.parser')).find_all('p')[0].get_text() + " " + (BeautifulSoup((requests.get("https://simple.wikipedia.org/wiki/" + ids)).content, 'html.parser')).find_all('p')[1].get_text())
        all_text.append(ids + "\n" + id_text)
    with open("/Users/solomondellapenna/Google Drive/pythonHW/" + file_name, "w") as file_handler:
         file_handler.write("\n\n".join(all_text))
    file_handler.close()
idlist = ["First", "Second", "Third", "Fourth", "Fifth"]
id_names(idlist)



# Interface with google docs api
# Parse out () and [] and within paragraphs COMPLETE
# Replace common words with synonyms 
# Ask how many ids
# Create web interface
# Host on AWS through kubernetes in docker container
