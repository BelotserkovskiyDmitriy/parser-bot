import sqlite3
import logging

import requests
from bs4 import BeautifulSoup

from config import page1
from db_func import create_connection, update_list, input_new_titles


def search_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    db_file = "flats_olx.db"

    all_flats = soup.find_all("tr", class_="wrap")
    flats_count = 0
    list_of_flats = []
    for td in all_flats:
        title_text = td.h3.get_text()

        if("новостр" in title_text or "Новостр" in title_text):
            flats_count += 1
            formated_title_text = ' '.join(title_text.split())
            list_of_flats.append(formated_title_text)

    db_connection = create_connection(db_file)
    actual_list = update_list(db_connection, list_of_flats)
    input_new_titles(db_connection, actual_list)

    # get description of newly announced flat
    list_of_descriptions = []
    for flat in actual_list:
        flat_link = td.h3.a['href']
        flat_page = requests.get(flat_link)
        soup_flat = BeautifulSoup(flat_page.content, 'html.parser')
        flat_description = soup_flat.find(id="textContent")
        text_description = flat_description.get_text()
        formated_description = ' '.join(text_description.split())
        list_of_descriptions.append(formated_description)

    print("Найдено новостройек - " + str(flats_count))
    print(actual_list)
    print(list_of_descriptions)
