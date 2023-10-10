import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import csv
cookies = {
    'event_user_hash': 'e58243c5-d5fe-45d2-8ef6-531f84a98879',
    '_gcl_au': '1.1.2037645886.1690456584',
    '_hjSessionUser_3562562': 'eyJpZCI6IjE2ZTNjMjU5LWRlY2EtNTVmZS05NTAwLThmYzc3NDY4NWQ0YiIsImNyZWF0ZWQiOjE2OTA0NTY1ODQxNTYsImV4aXN0aW5nIjp0cnVlfQ==',
    'lastAnalyticsEvent': 'listing:feed:listing:ad:view',
    'cf_clearance': 'Hd7vFe0wU6ucvWKEcJf5DZHaKH84rM5NPcPXLAVIAp4-1696414254-0-1-51a29480.483008b2.6a3cb60-0.2.1696414254',
    '_ga': 'GA1.1.218833040.1690456584',
    '_ga_Z4VRYJ4XGN': 'GS1.1.1696414254.5.1.1696414254.0.0.0',
    'experiment': 'novalue',
    'event_session_id': '965785b59f978d1c8999534783075dad',
    '_hjSession_3562562': 'eyJpZCI6ImY4ZTAzZTUxLWFlYjYtNDZjYi04NDliLWE4NDEyZDE0OGIyYiIsImNyZWF0ZWQiOjE2OTY0MTQzODM3NTUsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
    'device_fingerprint': '7f4864ede8cd9df387b3349ac6d1148b',
}

headers = {
    'authority': 'lalafo.kg',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'event_user_hash=e58243c5-d5fe-45d2-8ef6-531f84a98879; _gcl_au=1.1.2037645886.1690456584; _hjSessionUser_3562562=eyJpZCI6IjE2ZTNjMjU5LWRlY2EtNTVmZS05NTAwLThmYzc3NDY4NWQ0YiIsImNyZWF0ZWQiOjE2OTA0NTY1ODQxNTYsImV4aXN0aW5nIjp0cnVlfQ==; lastAnalyticsEvent=listing:feed:listing:ad:view; cf_clearance=Hd7vFe0wU6ucvWKEcJf5DZHaKH84rM5NPcPXLAVIAp4-1696414254-0-1-51a29480.483008b2.6a3cb60-0.2.1696414254; _ga=GA1.1.218833040.1690456584; _ga_Z4VRYJ4XGN=GS1.1.1696414254.5.1.1696414254.0.0.0; experiment=novalue; event_session_id=965785b59f978d1c8999534783075dad; _hjSession_3562562=eyJpZCI6ImY4ZTAzZTUxLWFlYjYtNDZjYi04NDliLWE4NDEyZDE0OGIyYiIsImNyZWF0ZWQiOjE2OTY0MTQzODM3NTUsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; device_fingerprint=7f4864ede8cd9df387b3349ac6d1148b',
    'dnt': '1',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://lalafo.kg/kyrgyzstan/nedvizhimost', cookies=cookies, headers=headers)


def get_source_html(url):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(5)

        block = driver.find_element(By.CLASS_NAME, 'virtual-scroll__container')
        action = ActionChains(driver)
        visited_elements = set()
        current_translateY = 0  # Исходное значение translateY

        while True:
            # Создаем уникальный ключ на основе текущего translateY значения
            unique_key = f'translateY_{current_translateY}'

            # Проверяем, есть ли элемент в множестве
            if unique_key not in visited_elements:
                # Если элемент уникален, добавляем его в множество и записываем в файл
                visited_elements.add(unique_key)

                # Находим элемент с текущим translateY значением
                target_div = block.find_element(By.CSS_SELECTOR,
                                                f'div[style="transform: translateY({current_translateY}px); position: absolute; width: 100%;"]')

                with open('target_div.html', 'a', encoding='utf-8') as file:
                    file.write(target_div.get_attribute('outerHTML'))
                    file.write('\n')  # Добавляем разделитель между содержимым

            # Увеличиваем текущее значение translateY на 186 для поиска следующего элемента
            current_translateY += 186

            # Скроллим к следующему элементу
            action.move_to_element(target_div).perform()
            time.sleep(5)

        # ________________________________________________________________________________________________

        # with open('target_div.html', 'r', encoding='utf-8') as file:
        #     html_content = file.read()
        #
        # soup = BeautifulSoup(html_content, 'html.parser')
        # ad_tiles = soup.find_all('div', class_='AdTileHorizontal')
        # ad_data_list = []
        #
        # for ad_tile in ad_tiles:
        #     title = ad_tile.find('a', class_='AdTileHorizontalTitle')
        #     title_text = title.text.strip() if title else "no data"
        #
        #     description = ad_tile.find('p', class_='AdTileHorizontalDescription')
        #     description_text = description.text.strip() if description else "no data"
        #
        #     kgs_price = ad_tile.find('p', class_='AdTileHorizontalPrice').find('span')
        #     kgs_price_text = kgs_price.text if kgs_price else "no data"
        #
        #     usd_price = ad_tile.find('span', class_='international-price')
        #     usd_price_text = usd_price.text if usd_price else "no data"
        #
        #     location = ad_tile.find('span', class_='meta-info__location')
        #     location_text = location.text.strip() if location else "no data"
        #
        #     date = ad_tile.find('span', class_='AdTileHorizontalDate')
        #     date_text = date.text.strip() if date else "no data"
        #
        #     url = ad_tile.find('a', class_='AdTileHorizontalTitle')['href'] if ad_tile.find(
        #         'a', class_='AdTileHorizontalTitle') else "no data"
        #
        #     data_for_sale = ["Продается квартира", "Продается дом", "Продается участок"]
        #
        #     if description_text in data_for_sale or description_text.endswith("на продажу"):
        #         ad_data = {
        #             "Название": title_text,
        #             "Продажа": description_text,
        #             "Цена сом": kgs_price_text,
        #             "Цена доллар": usd_price_text,
        #             "Местоположение": location_text,
        #             "Дата": date_text,
        #             "URL": 'https://lalafo.kg' + url
        #         }
        #
        #         # Дополнительный запрос для получения description_text
        #         data_response = requests.get('https://lalafo.kg' + url)
        #         data_soup = BeautifulSoup(data_response.content, 'html.parser')
        #
        #         ul_tags = data_soup.find('ul', class_='details-page__params css-tl517w')
        #
        #         district = ul_tags.find('p', class_='Paragraph secondary', string='Район:')
        #         district_text = district.find_next('a').text.strip() if district else "no data"
        #
        #         area = ul_tags.find('p', class_='Paragraph secondary', string='Площадь участка (соток):')
        #         area_text = area.find_next('p').text.strip() if area else "no data"
        #
        #         area2 = ul_tags.find('p', class_='Paragraph secondary', string='Площадь (м2):')
        #         area2_text = area2.find_next('p').text.strip() if area2 else "no data"
        #
        #         rooms = ul_tags.find('p', class_='Paragraph secondary', string='Количество комнат:')
        #         rooms_text = rooms.find_next('a').text.strip() if rooms else "no data"
        #
        #         description_wrap = data_soup.find('div', class_='description__wrap').find_next('p').find_all('span')
        #         description_wrap_text = [i.text.strip() for i in description_wrap]
        #
        #         ad_data["Район"] = district_text
        #         ad_data["Площадь участка (соток)"] = area_text
        #         ad_data["Площадь"] = area2_text
        #         ad_data["Количество комнат"] = rooms_text
        #         ad_data["Описание от объявления"] = description_wrap_text
        #
        #         ad_data_list.append(ad_data)
        #
        # # для просмотра в консоли
        # # for idx, ad_data in enumerate(ad_data_list, start=1):
        # #     print(f"Объявление {idx}: {ad_data}")
        #
        # with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        #     fieldnames = ['Название', 'Продажа', 'Цена сом', 'Цена доллар', 'Местоположение', 'Дата', 'URL', 'Район',
        #                   'Площадь участка (соток)', 'Площадь', 'Количество комнат', 'Описание от объявления']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #
        #     for ad_data in ad_data_list:
        #         writer.writerow(ad_data)

    except Exception as e:
        print(e)

    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html('https://lalafo.kg/kyrgyzstan/nedvizhimost')


if __name__ == "__main__":
    main()
