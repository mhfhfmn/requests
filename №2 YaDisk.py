"""
Программа запрашивает токен Яндекс API и путь к файлу или каталогу;
если выбран файл, она его загружает в корень Яндекс диска,
если выбран каталог она создает в корне Яндекс диска папку с таким же названием
и загружает в нее все файлы.
К сожалению, запрашиваемый каталог не должен содержать внутри себя каталогов(выдаст ошибку, дойдя до его обработки)
С этим разберусь чуть позже, надеюсь для зачета по ДЗ этого хватит.
Спасибо за проверку.
"""


import requests
import os



class YaUploader:
    def __init__(self, token: str):
        self.token = token




    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }




    def _get_upload_link(self,  file_name):
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = self.get_headers()
            params = {"path": file_name, "overwrite": "true"}
            response = requests.get(upload_url, headers=headers, params=params)
            return response.json()


    def upload_file(self, local_file):
        href = self._get_upload_link(local_file.split('\\')[-1]).get("href", "")
        response = requests.put(href, data=open(local_file, 'rb'))
        response.raise_for_status()


    def new_folder(self, path):
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {'path': path, 'overwrite': 'true'}
        response = requests.put(folder_url, headers=headers, params=params)

    def upload_file_in_derectory(self, local_file):
        path_to_upload = '{}/{}'
        href = self._get_upload_link(path_to_upload.format(local_file.split('\\')[-2], local_file.split('\\')[-1])).get("href", "")
        response = requests.put(href, data=open(local_file, 'rb'))
        response.raise_for_status()

    def upload_path(self, local_path):
        self.new_folder(local_path.split('\\')[-1])
        os.chdir(path_to_file)
        list_files = os.listdir()
        for file in list_files:
            file_path = f'''{local_path}\{file}'''
            self.upload_file_in_derectory(file_path)





def main():
    if os.path.exists(path_to_file):
        uploader = YaUploader(token)
        if os.path.isfile(path_to_file):
            uploader.upload_file(path_to_file)
            print('Файл загружен')
        elif os.path.isdir(path_to_file):
            uploader.upload_path(path_to_file)
            print('Каталог загружен')
    else:
        print('Файл или каталог не найден!')







if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу или каталогу: ')
    token = input('Введите Токен Яндекс API: ')
    main()
