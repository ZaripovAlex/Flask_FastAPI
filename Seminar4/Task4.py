# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте потоки.

import os
import threading
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

thread_list = []
for el in os.listdir(base):
    thread = threading.Thread(target=count_words, args=[os.path.join(base, el)])
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

