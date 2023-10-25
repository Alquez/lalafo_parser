import requests
import json
from bs4 import BeautifulSoup


def get_data():
    cookies = {
        'hl': 'ru',
        'device_view': 'full',
        '_gid': 'GA1.2.616341897.1692337111',
        '_gat': '1',
        '_ga_CFBCVF3CMM': 'GS1.1.1692339797.2.1.1692340628.0.0.0',
        '_ga': 'GA1.2.1297161967.1692337111',
        'show-banner-right-pos1': 'banner-4',
        'show-banner-right-pos2': 'banner-4',
        'show-banner-right-pos3': 'banner-4',
        'show-banner-branding': 'banner-1',
        'show-banner-top': 'banner-1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
                  'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'hl=ru; device_view=full; _gid=GA1.2.616341897.1692337111; _gat=1;
        # _ga_CFBCVF3CMM=GS1.1.1692339797.2.1.1692340628.0.0.0; _ga=GA1.2.1297161967.1692337111;
        # show-banner-right-pos1=banner-4; show-banner-right-pos2=banner-4; show-banner-right-pos3=banner-4;
        # show-banner-branding=banner-1; show-banner-top=banner-1',
        'DNT': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get('https://www.house.kg/snyat-kvartiru', cookies=cookies, headers=headers)
    if response.status_code == 200:
        with open('response_data.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        print("Ответ успешно записан в файл 'response_data.html'")
    else:
        print("Произошла ошибка при запросе")

#     # list_of_urls = []
#     # for page in range(1, 76):
#     #     responce = requests.get(f'https://www.house.kg/snyat-kvartiru?is_owner=1&sort_by=upped_at%20desc&page={page}',
#     #                         cookies=cookies, headers=headers).text
#     #     soup = BeautifulSoup(responce, 'html.parser')
#     #     dev = soup.find('div', class_='listings-wrapper')
#     #     urls = dev.find_all('meta', itemprop='url')
#     #
#     #     for url in urls:
#     #         full_url = url.get('content')
#     #         list_of_urls.append(full_url)
#     #
#     # with open('urls.txt', 'w') as file:
#     #     for url in list_of_urls:
#     #         file.write(f'https://www.house.kg{url}' + '\n')
#     #         print('done')
#
#     with open('urls.txt', 'r') as file:
#         lines = file.readlines()
#
#     data = []
#
#     for line in lines:
#         url = line.strip()  # Убираем лишние пробелы и символы новой строки
#         response = requests.get(url, cookies=cookies, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         main_info = soup.find('a', class_='ads-count').get_text('href')
#         additional_data = {}
#         try:
#             if main_info == '1 объявление пользователя' or main_info == '2 объявления пользователя':
#                 search_name = soup.find('div', class_='details-header')
#                 name = search_name.find('div', class_='left').find('h1').get_text().strip()
#
#                 try:
#                     address = search_name.find('div', class_='address').get_text().strip()
#                 except AttributeError:
#                     address = None
#
#                 search_price = soup.find('div', class_='sep main')
#                 price_dollar = search_price.find('div', class_='price-dollar').get_text().strip()
#                 price_som = search_price.find('div', class_='price-som').get_text().strip()
#
#                 number = soup.find('div', class_='number').get_text().strip()
#
#                 search_kvadratura = soup.find('div', class_='sep addit')
#                 kvadratura_price_dollar = search_kvadratura.find('div', class_='price-dollar').get_text().strip()
#                 kvadratura_price_som = search_kvadratura.find('div', class_='price-som').get_text().strip()
#
#                 a_tags = soup.find('div', class_='fotorama').find_all('a')
#                 images = [a_tag['href'] for a_tag in a_tags]
#
#                 search_description = soup.find('div', class_='description')
#                 if search_description:
#                     search_description = search_description.find('p').get_text().strip()
#
#                 for info_row in soup.find_all('div', class_='info-row'):
#                     label = info_row.find('div', class_='label').get_text().strip()
#                     info = info_row.find('div', class_='info').get_text().strip()
#                     info = ' '.join(info.split())
#                     additional_data[label] = info
#
#                 data.append({
#                     'Обьявления': main_info,
#                     'Название': name,
#                     'Адрес': address,
#                     'Ссылка': url,
#                     'Цена доллар': price_dollar,
#                     'Цена сом': price_som,
#                     'Квадратура доллар': kvadratura_price_dollar,
#                     'Квадратура сом': kvadratura_price_som,
#                     'Номер': number,
#                     'Описание от Арендодателя': search_description,
#                     'Данные': additional_data,
#                     'Фото': images,
#                 })
#         except:
#             pass
#
#         with open('elements.json', 'w', encoding='utf-8') as json_file:
#             json.dump(data, json_file, ensure_ascii=False, indent=4)
#
#
# def main():
#     get_data()
#
#
# if __name__ == '__main__':
#     main()


# import json
#
# # Читаем данные из файла file.json
# with open("file.json", "r") as input_file:
#     data = json.load(input_file)
#
# # Создаем пустой список для хранения элементов
# parsed_items = []
#
# # Цикл для перебора каждого элемента в списке items
# for item in data["items"]:
#     # Проверяем значение send_notification для каждого элемента
#     if item["send_notification"]:
#         # Добавляем элемент в список parsed_items
#         parsed_items.append(item)
#
# # Создаем новый объект данных с объединенными элементами
# merged_data = data.copy()
# merged_data["items"] = parsed_items
#
# # Записываем объединенные данные в один файл
# with open("merged_output_file.json", "w", encoding="utf-8") as output_file:
#     json.dump(merged_data, output_file, ensure_ascii=False, indent=4)
#     print("Объединенные данные успешно записаны в merged_output_file.json")

# merged_items = []
#
# for file_number in range(1, 10):
#     file_name = f"merged_output_file{file_number}.json"
#
#     try:
#         with open(file_name, "r", encoding="utf-8") as input_file:
#             file_data = json.load(input_file)
#             if "items" in file_data:
#                 merged_items.extend(file_data["items"])
#                 print(f"Файл {file_name} успешно добавлен.")
#     except FileNotFoundError:
#         print(f"Файл {file_name} не найден.")
#
# merged_data = {
#     "total": len(merged_items),
#     "items": merged_items
# }
#
# with open("merged_output_all.json", "w", encoding="utf-8") as output_file:
#     json.dump(merged_data, output_file, ensure_ascii=False, indent=4)
#     print("Объединенные данные успешно записаны в merged_output_all.json")
