# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте процессы.

import os
import multiprocessing
from datetime import time
import requests
from pathlib import Path

base = Path(__file__).resolve().parent.parent

def count_words(el: str):
    if os.path.isfile(os.path.join(base, el)):
        with open(el) as f:
            words = 0
            for line in f:
                words += len(line.strip(" ").split())
                print(f'В файле:{el}: {words} слов')

process = []

if __name__ == '__main__':
    start_time = time()
    for el in os.listdir(base):
        process.append(multiprocessing.Process(target=count_words, args=[os.path.join(base, el)]))
    for process in process:
        process.start()
    for process in process:
        process.join()
    print(f'Время выполнения {time() - start_time}')
