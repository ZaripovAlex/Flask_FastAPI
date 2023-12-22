# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте асинхронный подход.

import os
import asyncio
import aiofiles
from pathlib import Path

base = Path(__file__).resolve().parent


async def count_words(filename: str):
    file_path = os.path.join(base, filename)
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        words = 0
        for line in await f.readlines():
            words += len(line.strip().split())
            print(f'В файле:{filename}: {words} слов')


tasks = []

async def main():
    for el in os.listdir(base):
        task = asyncio.ensure_future(count_words(el))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
