import json
import requests
import csv
from bs4 import BeautifulSoup
import os
"""
Этот скрипт на Python собирает данные о недвижимости с веб-сайта "lalafo.kg". 
Он читает информацию из JSON-файла, отправляет запросы к веб-сайту для получения дополнительных данных, 
обрабатывает их и сохраняет в CSV-файле. 
Скрипт эффективно собирает и структурирует данные для последующего анализа или использования.
"""

cookies = {
    'event_user_hash': 'e58243c5-d5fe-45d2-8ef6-531f84a98879',
    '_gcl_au': '1.1.2037645886.1690456584',
    '_hjSessionUser_3562562': 'eyJpZCI6IjE2ZTNjMjU5LWRlY2EtNTVmZS05NTAwLThmYzc3NDY4NWQ0YiIsImNyZWF0ZWQiOjE2OTA0NTY1ODQxNTYsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.1.218833040.1690456584',
    'cf_clearance': 'bKFthv.YEPzX7nAw08_N9_FK0jL8NDofeqHSehbfV4k-1697438275-0-1-51a29480.e6adea6.6a3cb60-0.2.1697438275',
    '_hjIncludedInSessionSample_3562562': '0',
    '_hjSession_3562562': 'eyJpZCI6ImNkY2U5Y2ZhLTQwZTYtNDI1MC05ZGI4LWU2M2IzODBkNDhiZSIsImNyZWF0ZWQiOjE2OTc0MzgyNzU4NDcsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
    'experiment': 'novalue',
    'event_session_id': 'b2eb08fed9f6b8057d812c393304136b',
    '_fbp': 'fb.1.1697438295562.751024233',
    'lastAnalyticsEvent': 'listing:feed:listing:ad:view',
    '_ga_Z4VRYJ4XGN': 'GS1.1.1697438275.20.1.1697438934.0.0.0',
    '__gads': 'ID=0c29e5b7d02c2d25:T=1697438275:RT=1697438933:S=ALNI_MZQe-zybCc0YPOSV_KQC1f9Bnxj_g',
    '__gpi': 'UID=00000c99f511c8c7:T=1697438275:RT=1697438933:S=ALNI_MYQ8dKtU1UcZpOeJbFanQ0UiSmCNg',
    'device_fingerprint': '7f4864ede8cd9df387b3349ac6d1148b',
    'paid-background': '{%2212-1-0%22:{%22641%22:1}%2C%2212-2-2029%22:{%22645%22:2}}',
}

headers = {
    'authority': 'lalafo.kg',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer',
    # 'cookie': 'event_user_hash=e58243c5-d5fe-45d2-8ef6-531f84a98879; _gcl_au=1.1.2037645886.1690456584; _hjSessionUser_3562562=eyJpZCI6IjE2ZTNjMjU5LWRlY2EtNTVmZS05NTAwLThmYzc3NDY4NWQ0YiIsImNyZWF0ZWQiOjE2OTA0NTY1ODQxNTYsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.218833040.1690456584; cf_clearance=bKFthv.YEPzX7nAw08_N9_FK0jL8NDofeqHSehbfV4k-1697438275-0-1-51a29480.e6adea6.6a3cb60-0.2.1697438275; _hjIncludedInSessionSample_3562562=0; _hjSession_3562562=eyJpZCI6ImNkY2U5Y2ZhLTQwZTYtNDI1MC05ZGI4LWU2M2IzODBkNDhiZSIsImNyZWF0ZWQiOjE2OTc0MzgyNzU4NDcsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; experiment=novalue; event_session_id=b2eb08fed9f6b8057d812c393304136b; _fbp=fb.1.1697438295562.751024233; lastAnalyticsEvent=listing:feed:listing:ad:view; _ga_Z4VRYJ4XGN=GS1.1.1697438275.20.1.1697438934.0.0.0; __gads=ID=0c29e5b7d02c2d25:T=1697438275:RT=1697438933:S=ALNI_MZQe-zybCc0YPOSV_KQC1f9Bnxj_g; __gpi=UID=00000c99f511c8c7:T=1697438275:RT=1697438933:S=ALNI_MYQ8dKtU1UcZpOeJbFanQ0UiSmCNg; device_fingerprint=7f4864ede8cd9df387b3349ac6d1148b; paid-background={%2212-1-0%22:{%22641%22:1}%2C%2212-2-2029%22:{%22645%22:2}}',
    'country-id': '12',
    'device': 'pc',
    'dnt': '1',
    'experiment': 'novalue',
    'if-none-match': 'W/"5ee5f-cXqNpF8cd5KSmoiXnl0Ir/InvIA"',
    'language': 'ru_RU',
    'referer': 'https://lalafo.kg/kyrgyzstan/nedvizhimost',
    'request-id': 'react-client_80120b38-0f5e-4d6e-ae07-14ebe793b3e6',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'user-hash': 'e58243c5-d5fe-45d2-8ef6-531f84a98879',
}
params = {
    'expand': 'url',
    'page': '1',
}
csv_filename = 'Недвижимость.csv'

fields = ["Название", "Город", "Телефон", "Тип продажи", "Ссылка", "Район", "Площадь участка (соток):", "Площадь (м2):", "Количество комнат:", "Цена в долларе", "Цена в сомах"]

# Проверяем, существует ли файл. Если нет, создаем файл с заголовками
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', encoding='UTF-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

def write_to_csv(row):
    with open(csv_filename, 'a', encoding='UTF-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=row.keys())
        writer.writerow(row)


# Открываем JSON-файл с данными для чтения
with open('lalafo_data_no_duplicates.json', 'r', encoding='UTF-8') as file:
    data_list = json.load(file)
    try:
        with open(csv_filename, 'x', encoding='UTF-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data_list[0].keys())
            writer.writeheader()
    except FileExistsError:
        pass
    # Создаем пустой список для хранения отобранных данных
    selected_fields_list = []

    # Счетчик для отслеживания количества обработанных элементов
    count = 1

    # Проходимся по каждому элементу в списке данных
    for item in data_list:
        try:
            # Извлекаем необходимые поля из текущего элемента
            selected_fields = {
                "Название": item.get("title"),
                "Город": item.get("city"),
                "Телефон": item.get("mobile"),
                "Тип продажи": item.get("ad_label"),
                "Ссылка": f'https://lalafo.kg{item.get("url")}',
                "Район": None,
            }

            # Отправляем GET-запрос для получения дополнительных данных из веб-страницы
            data_response = requests.get(f'https://lalafo.kg{item.get("url")}', params=params, cookies=cookies,
                                         headers=headers)
            data_soup = BeautifulSoup(data_response.content, 'html.parser')

            # Извлекаем информацию о площади участка, площади и количестве комнат из HTML-страницы
            # (если соответствующие данные присутствуют)
            area = data_soup.find('p', class_='LFParagraph size-14', string='Площадь участка (соток):')
            area_text = area.find_next('p').text.strip() if area else ""
            selected_fields["Площадь участка (соток):"] = area_text

            area2 = data_soup.find('p', class_='LFParagraph size-14', string='Площадь (м2):')
            area2_text = area2.find_next('p').text.strip() if area2 else ""
            selected_fields["Площадь (м2):"] = area2_text

            rooms = data_soup.find('p', class_='LFParagraph size-14', string='Количество комнат:')
            rooms_text = rooms.find_next('a').text.strip() if rooms else ""
            selected_fields["Количество комнат:"] = rooms_text

            # Определяем цену в сомах и долларах в зависимости от валюты
            if item.get("currency") == 'KGS':
                selected_fields["Цена в сомах"] = item.get("price") if item.get("price") else ""
                selected_fields["Цена в долларе"] = ""
            elif item.get("currency") == 'USD':
                selected_fields["Цена в долларе"] = item.get("price") if item.get("price") else ""
                selected_fields["Цена в сомах"] = item.get("national_price").get("price") if item.get("price") else ""
            else:
                selected_fields["Цена в долларе"] = "Договорная"
                selected_fields["Цена в сомах"] = "Договорная"

            # Извлекаем район из параметров товара, если он присутствует
            for param in item.get("params", []):
                if param.get("name") == "Район":
                    selected_fields["Район"] = param.get("value")

            # Добавляем отобранные данные в список
            selected_fields_list.append(selected_fields)

            write_to_csv(selected_fields)

            # Выводим информацию о количестве обработанных элементов
            print(f"Обработано {count} из {len(data_list)}")
            count += 1

        # Обрабатываем исключения, если какие-либо данные не могут быть извлечены
        # Таким образом пропускаем исключение и продолжаем обработку следующего элемента
        except Exception as e:
            print(f"Элемент не найден в данном блоке. Пропускаем... https://lalafo.kg{item.get('url')}")
            continue
