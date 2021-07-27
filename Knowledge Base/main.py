"""
Prerequisites
- Python 3.9.X 
- PIP: python -m pip install -U pip
- NLTK: pip install nltk
- run python shell and then run: nltk.download()
- pip install pandas

Useful links:
- PIP: https://www.datacamp.com/community/tutorials/python-install-pip?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9061576&gclid=Cj0KCQjw9O6HBhCrARIsADx5qCQ_xRiO5QW6FYKz9WLddk8euDFY29ezo-jadSEIbB9PTRpQYeXCIFIaAhbAEALw_wcB
- NLTK: https://www.nltk.org/index.html
- Pandas: https://pandas.pydata.org/
"""

import nltk
from  nltk.tokenize import word_tokenize
import spacy
import pandas as pd
from options_menu import OptionsMenu as om


# Read story from txt file
def read_story(filename: str):
    with open(filename, encoding="utf8") as f:
        raw_data = f.readline()
    return raw_data

# Creates a list of all the words
def create_knowledge_base():
    data_source = read_story("Knowledge Base/story.txt")
    return word_tokenize(data_source)

# tagged = nltk.pos_tag(create_knowledge_base())
# print(tagged)

while True:
    menu_choice = om()
    
    try:
        choice = int(menu_choice.print_options_menu())

        if(choice == 1):
            pass

        if(choice == 2):
            pass

        if(choice == 3):
            exit(0)

        if(choice < 1 or choice > 3): 
            print("Oops! Invalid input, please select a choice from 1-3.")
            continue

    except ValueError:
        print("Oops! Invalid input, please select a choice from 1-3.")
        continue


