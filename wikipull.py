import requests
from bs4 import BeautifulSoup
import sys
import re

def id_names():
    n_of_ids = int(input("How many Id's? "))
    file_name = input("Page Title: ") + ".txt"
    all_text = list()
    n = list(range(n_of_ids))
    i = 0
    while (n_of_ids > i):
        ids = (input(str(n[i] + 1) + " Id: "))
        try:
            id_text = re.sub(r" ?\[[^]]+\] | ?\([^)]+\)","",(BeautifulSoup((requests.get("https://simple.wikipedia.org/wiki/" + ids)).content, 'html.parser')).find_all('p')[0].get_text() + " " + (BeautifulSoup((requests.get("https://simple.wikipedia.org/wiki/" + ids)).content, 'html.parser')).find_all('p')[1].get_text())
        except:
            id_text = ""
        all_text.append(ids + "\n" + id_text)
        i += 1
    with open("/Users/solomondellapenna/Google Drive/pythonHW/" + file_name, "w") as file_handler:
         file_handler.write("\n\n".join(all_text))
    file_handler.close()
id_names()



# Interface with google drive api/library
# Parse out () and [] and within paragraphs COMPLETE
# Replace common words with synonyms MACHINE LEARNING?????
# Ask how many ids COMPLETE
# Create web interface
# Host on AWS through kubernetes in docker container
# Handle "odd" inputs COMPLETE (hopefully)
