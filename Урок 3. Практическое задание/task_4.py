"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import urllib.request
from hashlib import sha256


class PageHash():
    def __init__(self):
        self.hashed_data = {}

    def put_page(self, url_param, page_data):
        self.hashed_data[sha256(url_param.encode()).hexdigest()] = page_data

    def get_page(self, url_param):
        return self.hashed_data[sha256(url_param.encode()).hexdigest()]

    def check_page(self, url_param):
        if sha256(url_param.encode()).hexdigest() in self.hashed_data.keys():
            return True
        else:
            return False


url = "https://geekbrains.ru/"
my_hash = PageHash()
if not my_hash.check_page(url):
    print("not found, putting page content into hash")
    page = urllib.request.urlopen(url)
    my_hash.put_page(url, page.read())
else:
    print("already in hash. here is the page from hash")
    print(my_hash.get_page(url))


if not my_hash.check_page(url):
    print("not found, putting page content into hash")
    page = urllib.request.urlopen(url)
    my_hash.put_page(url, page.read())
else:
    print("already in hash. here is the page from hash")
    print(my_hash.get_page(url))
