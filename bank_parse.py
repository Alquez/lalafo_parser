import requests

cookies = {
    'token': 'eyJpdiI6Inhsc21kZTJJbk4xVkhOR2hmZ1hrWlE9PSIsInZhbHVlIjoiaVNhakFlV3dHVjlSODJcL2lVQzQ0cVRqdDZpQlB6bFhoVktob3ZnMnoyRFdlVDdPckVEVzk0UjNQQkdMQ3U3cEVPeXpFREJSVVwvWVgwUVo5YXBQZ0NUd0NETzByNFIyUG5mNkg5YlBuXC9FODA9IiwibWFjIjoiYzkzZDAzNjMwZDBjMWM0MWJiOTk1YzEyN2UzN2Q4ZGI0MjY3NzU2NmY0ZGQwMmYxOWNiZjRmYmU4YmUzMGU1YiJ9',
    'LSW_WEB': 'IR-CA-Application01',
    'cookiesession1': '678B286F62042E6AAFD1C587D522F6BD',
    'XSRF-TOKEN': 'eyJpdiI6IlB0UHU1aU1RRTFJRmVYVTQ2VThMbWc9PSIsInZhbHVlIjoiVXRzVVwvOVVEaTRzVWRqa2w1MlR6RUdOeG9Ja3VZVnkrdWVhTlRTQ1NLVmJKY2FyVEUrakl0NHVcL3VcL3FwSHJHa0ZOZ1c5Q0g5bmJ6U1dpMzU4OHZiMEE9PSIsIm1hYyI6ImMzNmJlODI4M2VhYTAzYzY4YWNlYzkwMDYwYTg4MjQ5MDczOTVhMGZiNmQ3NGY4NjA2ODY1MWUyNDUyMmFkYWYifQ%3D%3D',
    'irkzadmin_session': 'eyJpdiI6IjZZWTl1VlJ6NkdVWDZLQ04wenNRNUE9PSIsInZhbHVlIjoiWE1lMERZVGs0V2dicEpOYlFTbnJVVGZvbkZjNHhJZDVTQ3p4c0NuZldzWDVnSVNYVjF6OXA2MEJic01cLzdwalc5MUU2dkkzeHZJU3g2aHVnZ2VTWmNBPT0iLCJtYWMiOiIzMGI4MTc2M2FhYTViZTk2ZDg5YWQxNjFlNzQ1ZGUyNjk4ZTBiYTZkYzg5NTQxZDFlZjk2YzIxZWU4OGI5Njc1In0%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'token=eyJpdiI6Inhsc21kZTJJbk4xVkhOR2hmZ1hrWlE9PSIsInZhbHVlIjoiaVNhakFlV3dHVjlSODJcL2lVQzQ0cVRqdDZpQlB6bFhoVktob3ZnMnoyRFdlVDdPckVEVzk0UjNQQkdMQ3U3cEVPeXpFREJSVVwvWVgwUVo5YXBQZ0NUd0NETzByNFIyUG5mNkg5YlBuXC9FODA9IiwibWFjIjoiYzkzZDAzNjMwZDBjMWM0MWJiOTk1YzEyN2UzN2Q4ZGI0MjY3NzU2NmY0ZGQwMmYxOWNiZjRmYmU4YmUzMGU1YiJ9; LSW_WEB=IR-CA-Application01; cookiesession1=678B286F62042E6AAFD1C587D522F6BD; XSRF-TOKEN=eyJpdiI6IlB0UHU1aU1RRTFJRmVYVTQ2VThMbWc9PSIsInZhbHVlIjoiVXRzVVwvOVVEaTRzVWRqa2w1MlR6RUdOeG9Ja3VZVnkrdWVhTlRTQ1NLVmJKY2FyVEUrakl0NHVcL3VcL3FwSHJHa0ZOZ1c5Q0g5bmJ6U1dpMzU4OHZiMEE9PSIsIm1hYyI6ImMzNmJlODI4M2VhYTAzYzY4YWNlYzkwMDYwYTg4MjQ5MDczOTVhMGZiNmQ3NGY4NjA2ODY1MWUyNDUyMmFkYWYifQ%3D%3D; irkzadmin_session=eyJpdiI6IjZZWTl1VlJ6NkdVWDZLQ04wenNRNUE9PSIsInZhbHVlIjoiWE1lMERZVGs0V2dicEpOYlFTbnJVVGZvbkZjNHhJZDVTQ3p4c0NuZldzWDVnSVNYVjF6OXA2MEJic01cLzdwalc5MUU2dkkzeHZJU3g2aHVnZ2VTWmNBPT0iLCJtYWMiOiIzMGI4MTc2M2FhYTViZTk2ZDg5YWQxNjFlNzQ1ZGUyNjk4ZTBiYTZkYzg5NTQxZDFlZjk2YzIxZWU4OGI5Njc1In0%3D',
    'DNT': '1',
    'Referer': 'https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'beginDate': '20.10.2023',
    'endDate': '24.10.2023',
    'rates[]': [
        '1',  # '1': 'АВСТРАЛИЙСКИЙ ДОЛЛАР (AUD)',
        '48',  # '48': 'АЗЕРБАЙДЖАНСКИЙ МАНАТ (AZN)',
        '51',  # '51': 'АРМЯНСКИЙ ДРАМ (AMD)',
        '38',  # '38': 'БЕЛОРУССКИЙ РУБЛЬ (BYN)',
        '46',  # '46': 'БРАЗИЛЬСКИЙ РЕАЛ (BRL)',
        '42',  # '42': 'ВЕНГЕРСКИЕ ФОРИНТЫ (HUF)',
        '45',  # '45': 'ГОНКОНГСКИЙ ДОЛЛАР (HKD)',
        '52',  # '52': 'ГРУЗИНСКИЙ ЛАРИ (GEL)',
        '3',  # '3': 'ДАТСКАЯ КРОНА (DKK)',
        '4',  # '4': 'ДИРХАМ ОАЭ (AED)',
        '5',  # '5': 'ДОЛЛАР США (USD)',
        '6',  # '6': 'ЕВРО (EUR)',
        '49',  # '49': 'ИНДИЙСКАЯ РУПИЯ (INR)',
        '53',  # '53': 'ИРАНСКИЙ РИАЛ (IRR)',
        '7',  # '7': 'КАНАДСКИЙ ДОЛЛАР (CAD)',
        '8',  # '8': 'КИТАЙСКИЙ ЮАНЬ (CNY)',
        '9',  # '9': 'КУВЕЙТСКИЙ ДИНАР (KWD)',
        '10',  # '10': 'КЫРГЫЗСКИЙ СОМ (KGS)',
        '47',  # '47': 'МАЛАЗИЙСКИЙ РИНГГИТ (MYR)',
        '54',  # '54': 'МЕКСИКАНСКИЙ ПЕСО (MXN)',
        '13',  # '13': 'МОЛДАВСКИЙ ЛЕЙ (MDL)',
        '14',  # '14': 'НОРВЕЖСКАЯ КРОНА (NOK)',
        '39',  # '39': 'ПОЛЬСКИЙ ЗЛОТЫЙ (PLN)',
        '15',  # '15': 'РИЯЛ САУДОВСКОЙ АРАВИИ (SAR)',
        '16',  # '16': 'РОССИЙСКИЙ РУБЛЬ (RUB)',
        '17',  # '17': 'СДР (XDR)',
        '18',  # '18': 'СИНГАПУРСКИЙ ДОЛЛАР (SGD)',
        '44',  # '44': 'ТАДЖИКСКИЙ СОМОНИ (TJS)',
        '50',  # '50': 'ТАЙСКИЙ БАТ (THB)',
        '41',  # '41': 'ТУРЕЦКАЯ ЛИРА (TRY)',
        '20',  # '20': 'УЗБЕКСКИЙ СУМ (UZS)',
        '21',  # '21': 'УКРАИНСКАЯ ГРИВНА (UAH)',
        '2',  # '2': 'ФУНТ СТЕРЛИНГОВ СОЕДИНЕННОГО КОРОЛЕВСТВА (GBP)',
        '43',  # '43': 'ЧЕШСКАЯ КРОНА (CZK)',
        '22',  # '22': 'ШВЕДСКАЯ КРОНА (SEK)',
        '23',  # '23': 'ШВЕЙЦАРСКИЙ ФРАНК (CHF)',
        '40',  # '40': 'ЮЖНО-АФРИКАНСКИЙ РАНД (ZAR)',
        '25',  # '25': 'ЮЖНО-КОРЕЙСКИЙ ВОН (KRW)',
        '26'  # '26': 'ЯПОНСКАЯ ЙЕНА (JPY)'
    ],
}

response = requests.get(
    'https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut/excel',
    params=params,
    cookies=cookies,
    headers=headers,
)
file_path = 'rk_bank.xlsx'
# Проверяем, успешно ли выполнен запрос
if response.status_code == 200:
    # Сохраняем содержимое файла в указанный путь
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f'Файл успешно скачан и сохранен по пути: {file_path}')
else:
    print(f'Ошибка при скачивании файла. Код состояния: {response.status_code}')

# -------------------------------- -------------------------------- --------------------------------
data = {
    'format': 'XLS',
    'FROM_MONTH': '27.09.2023',
    'TO_YEAR': '27.10.2023',
    'lang': 'ru',
    'rates': '',
    'date': '27.09.2023 - 27.10.2023',
}

response = requests.post(
    'https://cbu.uz/common/arkhiv_valut/excel.php',
    cookies=cookies,
    headers=headers,
    data=data
)

file_path = 'uz_bank.xlsx'
# Проверяем, успешно ли выполнен запрос
if response.status_code == 200:
    # Сохраняем содержимое файла в указанный путь
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f'Файл успешно скачан и сохранен по пути: {file_path}')
else:
    print(f'Ошибка при скачивании файла. Код состояния: {response.status_code}')
