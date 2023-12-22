# Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.
import os
import threading
from datetime import time
import requests
from pathlib import Path

urls = ['https://www.google.ru/',
'https://gb.ru/',
'https://ya.ru/',
'https://www.python.org/',
'https://habr.com/ru/all/',
'https://mail.ru/',
'https://github.com/',
'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
'https://news.e1.ru/',
'https://www.1tv.ru/']

base = Path(__file__).resolve().parent
save_path = os.path.join(base, 'save')
if not os.path.exists(save_path):
    os.mkdir(save_path)
def download_page(url: str):
    response = requests.get(url)
    filename = url.replace('https://','').replace('.', '_').replace('/', '_') + '.html'
    with open(os.path.join(save_path, filename), 'wb') as f:
        f.write(response.text.encode('utf-8'))

thread_list = []
start_time = time()
for url in urls:
    thread = threading.Thread(target=download_page, args=(url,))
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()
print(f'Время выполнения {time() - start_time}')

