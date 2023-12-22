# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные
# файлы.
# Используйте процессы.


import os
import multiprocessing
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
save_path = os.path.join(base, 'save_processes')
if not os.path.exists(save_path):
    os.mkdir(save_path)
def download_page(url: str):
    response = requests.get(url)
    filename = url.replace('https://','').replace('.', '_').replace('/', '_') + '.html'
    with open(os.path.join(save_path, filename), 'wb') as f:
        f.write(response.text.encode('utf-8'))

processes = []

if __name__ == '__main__':
    start_time = time.time()
    for url in urls:
        process = multiprocessing.Process(target=download_page, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(f'Время выполнения {time.time() - start_time}')
