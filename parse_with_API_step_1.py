import requests
import json

"""
Скрипт собирает данные о недвижимости с веб-сайта "lalafo.kg". 
Сначала он отправляет запросы к API сайта для получения информации о недвижимости и 
сохраняет данные в файл. Затем скрипт удаляет дубликаты записей на основе уникальных идентификаторов 
с сохранением уникальных данных в json файл. 
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


def get_total_pages(category_id):
    params = {
        'category_id': category_id,
        'page': '1',
        'expand': 'url',
    }
    response = requests.get('https://lalafo.kg/api/search/v3/feed/search', params=params, cookies=cookies,
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_items = data["_meta"]["pageCount"]
        return total_items


def get_data_for_category(category_id):
    total_pages = get_total_pages(category_id)
    all_items = []
    count = 1
    for page in range(1, total_pages + 1):
        params = {
            'category_id': category_id,
            'page': str(page),
            'expand': 'url',
        }
        response = requests.get('https://lalafo.kg/api/search/v3/feed/search', params=params, cookies=cookies,
                                headers=headers)
        if response.status_code == 200:
            data = response.json()
            all_items.extend(data['items'])
            print(count, total_pages)
            count += 1
        else:
            print(f"Ошибка запроса на странице {page} для категории {category_id}. Статус код: {response.status_code}")

    return all_items

list_category = ['2038', '2046', '2031', '2055']
all_data = []

for category in list_category:
    data = get_data_for_category(category)
    all_data.extend(data)

# Сохранение всех данных в JSON-файле
with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
    json.dump(all_data, file, indent=2, ensure_ascii=False)

print("Данные успешно сохранены в lalafo_data.json.")

# Удаление дубликатов по полю 'id'
with open('lalafo_data.json', 'r', encoding='UTF-8') as file:
    data_list = json.load(file)

    # Создание множества для хранения уникальных ID
    unique_ids = set()

    # Создание нового списка объектов без дубликатов
    unique_data_list = []

    for item in data_list:
        item_id = item.get('id')

        # Проверка, есть ли такой ID в множестве уникальных ID
        if item_id not in unique_ids:
            unique_ids.add(item_id)  # Добавление ID в множество уникальных ID
            unique_data_list.append(item)  # Добавление объекта в новый список без дубликатов

# Сохранение данных без дубликатов в JSON-файле
with open('lalafo_data_no_duplicates.json', 'w', encoding='UTF-8') as file:
    json.dump(unique_data_list, file, indent=2, ensure_ascii=False)

print("Дубликаты успешно удалены. Уникальные данные сохранены в lalafo_data_no_duplicates.json.")

