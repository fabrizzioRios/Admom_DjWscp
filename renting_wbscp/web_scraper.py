import time

import requests
from lxml import html
from async_request import main_async
import asyncio

def main():
    list_of_names = []
    i = 0
    url_connection = requests.post("https://www.zankyou.com.mx/salones-bodas/ciudad/guadalajara")
    content_page = url_connection.text
    splitted_data = content_page.split('"')
    for element in splitted_data:
        if element == 'card-brief__title':
            room_name = splitted_data[i + 2]
            list_of_names.append(room_name)
        i += 1

    return list_of_names


def buy_place(min_budget, max_budget):

    i = 0
    list_places = []
    url = "https://www.flat.mx/venta/casas-en-guadalajara-zapopan"
    search_url = "https://www.flat.mx/propiedades"
    url_connection = requests.get(url)
    root = html.fromstring(url_connection.content)
    link = root.xpath(f'//*[@id="PhotoSlider"]/div/div/div[1]/div[1]/div/a/@href')

    for i in range(15):
        if i > 0:
            name = root.xpath(f'//*[@id="properties"]/div[{i}]/a/div/div[1]/h2/text()')
            price = root.xpath(f'//*[@id="properties"]/div[{i}]/a/div/div[3]/p/span/text()')

            raw_price = price[0].split('$')
            new_raw = raw_price[1].split(',')
            final_price = new_raw[0] + new_raw[1] + new_raw[2]
            complete_link = search_url + link[i - 1]
            if int(min_budget) <= int(final_price) <= int(max_budget):
                place_content = {
                    'name': name[0],
                    'price': final_price,
                    'link': complete_link,
                    'img': f'img_{i}.avif'
                }
                list_places.append(place_content)
    return list_places


def buy_terrain(min_budget, max_budget):
    list_of_terrains = []
    all_terrain_links = []
    new_price = []
    url = "https://inmuebles.mercadolibre.com.mx/terrenos/venta/jalisco/"
    url_connection = requests.get(url)
    root = html.fromstring(url_connection.content)
    all_terrain_names = root.xpath('//h2[contains(@class, "ui-search-item__title shops__item-title")]/text()')
    all_terrain_prices = root.xpath('//span[contains(@class, "price-tag-text-sr-only")]/text()')
    round_value = len(all_terrain_names) / 3
    # link scraping
    for i in range(int(round_value) + 1):
        for j in range(4):
            if i > 0 and j > 0:
                terrain_url_list = root.xpath(f'//*[@id="root-app"]/div/div[2]/section/ol[{i}]/li[{j}]/div/div/div['
                                              f'2]/div/div[3]/a/@href')
                terrain_link_url = terrain_url_list[0]
                all_terrain_links.append(terrain_link_url)
    # price formated
    for price in all_terrain_prices:
        real_price = price.split(' ')
        new_price.append(real_price[0])

    for index in range(len(all_terrain_names)):
        if int(min_budget) <= int(new_price[index]) <= int(max_budget):
            terrain_information = {
                'name': all_terrain_names[index],
                'price': new_price[index],
                'link': all_terrain_links[index],
                'img': f'img_{index + 1}.jpg'
            }
            list_of_terrains.append(terrain_information)
    return list_of_terrains


def house_renting(min_budget, max_budget):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    images = loop.run_until_complete(main_async())

    list_of_houses = []
    url = "https://www.casasyterrenos.com/jalisco/zapopan/terrenos/venta"
    url_connection = requests.get(url)
    root = html.fromstring(url_connection.content)
    all_houses_names = root.xpath('//div[contains(@class, "information")]//h3')
    all_houses_prices = root.xpath('//p[contains(@class, "price ")]')
    all_houses_links = root.xpath('//a[@rel="noopener noreferrer"]')
    print(images)
    print(all_houses_names)

    for index in range(len(all_houses_names)):
        if index > 0:
            print(all_houses_names[index].text_content())
            print(images[index])
            final_str = str()
            split_prices = all_houses_prices[index].text_content().split(' ')
            new_number = split_prices[1]
            number_concatenate = new_number.split(',')
            for number in number_concatenate:
                final_str = final_str + number
            int_number = int(final_str)
            if int(min_budget) <= int_number <= int(max_budget):
                house_information = {
                    'name': all_houses_names[index].text_content(),
                    'price': all_houses_prices[index].text_content(),
                    'link': f"https://www.casasyterrenos.com{all_houses_links[index + 2].get('href')}",
                    'img': images[index]
                }
                list_of_houses.append(house_information)
    return list_of_houses


if __name__ == '__main__':
    house_renting(0, 100000000)

