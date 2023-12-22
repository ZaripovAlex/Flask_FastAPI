# Задание №7
# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import random
import time
import asyncio
import aiofiles
import os

def arr_generator(n: int = 1000000):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 100))
    return arr


def split_the_array(arr: list, n: int):
    arr_parts = []
    coef = len(arr) // n
    start = 0
    end = 0
    for _ in range(coef):
        if end <= (len(arr) - 1):
            end += coef
            arr_parts.append((start, end - 1))
            start = end
    # print(arr_parts)
    return arr_parts


def sum_the_array(arr: list, start: int, end: int):
    sum = 0

    for i in range(start, end):
        sum += arr[i]
    with open("sum.txt", "a") as f:
        f.write(str(sum) + '\n')



async def main():
    rez = []
    tasks = []
    arr = arr_generator(1_000_000)
    arr1 = split_the_array(arr, 100)
    for i in arr1:
        task = asyncio.create_task(sum_the_array(arr, i[0], i[1],))
        tasks.append(task)
    start_time = time.time()
    await asyncio.gather(*tasks)
    print(f'Время выполнения {time.time()-start_time}')
    async with aiofiles.open("sum.txt", "r") as f:
        for line in await f.readlines():
            rez.append(int(line.strip()))
    os.remove("sum.txt")
    print(sum(rez))

if __name__ == '__main__':
    asyncio.run(main())