import requests
from bs4 import BeautifulSoup

from db_func import create_connection, update_list, input_new_titles
from headlines import get_headlines


def get_flats_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    db_file = "flats_olx.db"

    # Search all novostroys and add them into the list
    all_flats = soup.find_all("tr", class_="wrap")
    list_of_novostroys = []
    for td in all_flats:
        current_title = td.h3
        title_text = td.h3.get_text()

        if("новостр" in title_text or "Новостр" in title_text):
            # formated_title_text = ' '.join(title_text.split())
            # list_of_flats.append((formated_title_text,))
            link_of_novostroy = current_title.a['href']
            list_of_novostroys.append(link_of_novostroy)

    # Then check DB. Delete links from list if they are already in the list
    # and add in DB new links

    db_connection = create_connection(db_file)
    actual_list = update_list(db_connection, list_of_novostroys)

    # Get headers from all novostroys
    flats_info = get_headlines(actual_list)

    input_new_titles(db_connection, flats_info)

    return flats_info


# search_title('https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/kharkov/')
