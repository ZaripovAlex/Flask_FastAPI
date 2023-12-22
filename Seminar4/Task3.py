# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# После загрузки данных нужно записать их в отдельные
# файлы.
# Используйте асинхронный подход.

import os
from datetime import time

import aiohttp
import asyncio
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
save_path = os.path.join(base, 'save_async')
if not os.path.exists(save_path):
    os.mkdir(save_path)

async def download_page(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = url.replace('https://','').replace('.', '_').replace('/', '_') + '.html'
            content = await response.text()
            with open(os.path.join(save_path, filename),'w',encoding= "utf-8") as f:
                f.write(content)

async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_page(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Время выполнения {time.time() - start_time}')