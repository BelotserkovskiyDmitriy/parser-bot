import requests
from bs4 import BeautifulSoup

from api_functions import make_telegraf_page


def get_headlines(list_of_flats_links):
    # List of dicts, with all flats data
    general_objects_info = []

    for link in list_of_flats_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        object_info = {}

        object_info['url'] = link

        # Get photos
        list_of_photos_links = []
        photos_links = soup.find('ul', id='descGallery')
        all_links = photos_links.find_all('a')
        for a in all_links:
            photo_link = a['href']
            list_of_photos_links.append(photo_link)
        object_info['photos'] = list_of_photos_links

        # images = get_images(list_of_photos_links)
        # print(images)
        telegraf_link = make_telegraf_page(list_of_photos_links)
        object_info['telegraf_link'] = telegraf_link

        # adress of object
        flat_adress = soup.find("div", class_="offer-user__address").get_text()
        formated_flat_adress = ' '.join(flat_adress.split())
        object_info['flat_adress'] = formated_flat_adress

        # price of object
        flat_price = soup.find("div", class_="pricelabel").get_text()
        formated_flat_price = ' '.join(flat_price.split())
        object_info["flat_price"] = formated_flat_price

        # # id of announcement
        all_bottombar_li = soup.find_all("li", class_="offer-bottombar__item")
        announcement_id = all_bottombar_li[-1].strong.get_text()
        object_info['object_id'] = announcement_id

        # other info for bot`s post
        all_titles = soup.find_all("li", class_="offer-details__item")
        for li in all_titles:
            text_of_title = li.get_text()
            if("Количество комнат" in text_of_title):
                rooms_count = li.strong.get_text()
                object_info['rooms_count'] = rooms_count
            elif("Общая площадь" in text_of_title):
                flat_area = li.strong.get_text()
                object_info['flat_area'] = flat_area
            elif("Этажность" in text_of_title):
                total_floors = li.strong.get_text()
                object_info['total_floors'] = total_floors
            elif("Этаж" in text_of_title):
                flat_floor = li.strong.get_text()
                object_info['flat_floor'] = flat_floor

            # get images
            else:
                True

        general_objects_info.append(object_info)

    return general_objects_info


def get_images(list):
    list_of_processed_images = []

    for link in list:
        response = requests.get(link)
        list_of_processed_images.append(response.content)

    return list_of_processed_images







#
# lis = ['https://www.olx.ua/obyavlenie/sdaetsya-2-kom-kvartira-v-novostroe-zhk-pavlovskiy-kvartal-IDKe7jK.html#80a727ef8d', 'https://www.olx.ua/obyavlenie/sdam-svoyu-1komn-kv-nauchnaya-ul-lopanskaya-31-novostroy-IDKayal.html#80a727ef8d;promoted']
#
# get_headlines(lis)
