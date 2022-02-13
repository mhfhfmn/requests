"""
https://curlconverter.com/#python





#curl -X GET --header 'Accept: application/json' --header 'Authorization: OAuth AQAAAABdQYihAADLW-kcmghJMEY7lfJZUpFynMA' 'https://cloud-api.yandex.net/v1/disk/resources?path=%2F'

import requests
from pprint import pprint

headers = {
    'Accept': 'application/json',
    'Authorization': 'OAuth AQAAAABdQYihAADLW-kcmghJMEY7lfJZUpFynMA',
}

params = (
    ('path', '/'),
)

response = requests.get('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)

pprint(response.json())



"""


token = 'AQAAAABdQYihAADLW-kcmghJMEY7lfJZUpFynMA'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        pass
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к файлу: ')
    token = input('Введите token: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
