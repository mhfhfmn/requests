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
