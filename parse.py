import requests
import json

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
    'category_id': '2038',
    'expand': 'url',
}
# file_paths = ['lalafo_data.json', 'lalafo_data2.json', 'lalafo_data3.json', 'lalafo_data4.json']
# combined_data = []
#
# for file_path in file_paths:
#     with open(file_path, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#         combined_data.extend(data)  # Объединяем данные в один список
#
# # Сохраняем объединенные данные в новом файле
# with open('combined_lalafo_data.json', 'w', encoding='UTF-8') as outfile:
#     json.dump(combined_data, outfile, indent=2, ensure_ascii=False)
#
# print("Данные успешно объединены и сохранены в combined_lalafo_data.json.")
# response = requests.get('https://lalafo.kg/api/search/v3/feed/search', params=params, cookies=cookies, headers=headers)
# data = response.json()
# all_data = []


#def get_data():
#    page = 1
#    all_items = []  # Создаем пустой список для всех элементов
#
#    for i in range(259):
#        params['page'] = str(page)
#        response = requests.get('https://lalafo.kg/api/search/v3/feed/search', params=params, cookies=cookies,
#                                headers=headers)
#
#        # Проверяем статус код ответа
#        if response.status_code != 200:
#            print(f"Ошибка запроса. Статус код: {response.status_code}")
#            break
#
#        data = response.json()
#
        # Проверяем, есть ли поле 'items' в текущем JSON-ответе
#        if 'items' in data and data['items']:
            # Если есть, добавляем элементы текущей страницы в общий список
#            all_items.extend(data['items'])
#        else:
            # Если следующей страницы нет, завершаем выполнение цикла
#            break

        # Проверяем, есть ли следующая страница
#        if '_links' in data and 'next' in data['_links']:
#            page += 1
#        else:
            # Если следующей страницы нет, завершаем выполнение цикла
#            break

#    return all_items


# Получаем все элементы данных
#all_data = get_data()

# Сохраняем все данные в один JSON-файл
#with open('lalafo_data4.json', 'w', encoding='UTF-8') as file:
#    json.dump(all_data, file, indent=2, ensure_ascii=False)

#print("Данные успешно сохранены в lalafo_data4.json.")


# with open('lalafo_data_no_duplicates.json', 'r', encoding='UTF-8') as file:
#    # Загружаем данные как список объектов JSON
#    data_list = json.load(file)
#    print(len(data_list))

# import json
#
# with open('lalafo_data_no_duplicates.json', 'r', encoding='UTF-8') as file:
#     # Загружаем данные как список объектов JSON
#     data_list = json.load(file)
#
#     # Создаем новый список для первых 10 объектов
#     first_10_objects = data_list[:500]
#
# # Сохраняем первые 10 объектов в JSON-файл
# with open('first_500_objects.json', 'w', encoding='UTF-8') as file:
#     json.dump(first_10_objects, file, indent=2, ensure_ascii=False)

# import json

# with open('combined_lalafo_data.json', 'r', encoding='UTF-8') as file:
#     # Загружаем данные как список объектов JSON
#     data_list = json.load(file)
#
#     # Проверяем наличие дубликатов по полю 'id'
#     unique_ids = set()  # Создаем пустое множество для уникальных ID
#
#     for item in data_list:
#         item_id = item.get('id')
#         if item_id in unique_ids:
#             print(f"Найден дубликат по ID: {item_id}")
#         else:
#             unique_ids.add(item_id)  # Добавляем ID в множество уникальных ID
#
#     print(f"Количество уникальных объектов по полю 'id': {len(unique_ids)}")

# with open('combined_lalafo_data.json', 'r', encoding='UTF-8') as file:
#     # Загружаем данные как список объектов JSON
#     data_list = json.load(file)
#
#     # Создаем пустое множество для уникальных ID
#     unique_ids = set()
#
#     # Создаем новый список для объектов без дубликатов
#     unique_data_list = []
#
#     for item in data_list:
#         item_id = item.get('id')
#
#         # Проверяем, есть ли такой ID в множестве уникальных ID
#         if item_id not in unique_ids:
#             unique_ids.add(item_id)  # Добавляем ID в множество уникальных ID
#             unique_data_list.append(item)  # Добавляем объект в новый список без дубликатов
#
# # Сохраняем данные без дубликатов в JSON-файл
# with open('lalafo_data_no_duplicates.json', 'w', encoding='UTF-8') as file:
#     json.dump(unique_data_list, file, indent=2, ensure_ascii=False)
#
# print("Дубликаты успешно удалены. Уникальные данные сохранены в lalafo_data_no_duplicates.json.")