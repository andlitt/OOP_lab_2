#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from money_package import Money_task_2

if __name__ == "__main__":
    # Создаем объекты Money разными способами
    m1 = Money_task_2(123.45)
    m2 = Money_task_2("123.45")
    m3 = Money_task_2(12345)
    m4 = Money_task_2([5, 4, 3, 2, 1])

    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print(f"m3: {m3}")
    print(f"m4: {m4}\n")

    # Тестируем индексацию
    print(f"m1[0]: {m1[0]}")
    print(f"m1[1]: {m1[1]}")
    print(f"m1[2]: {m1[2]}\n")

    # Тестируем размер и количество
    print(f"m1 размер: {m1.size()}")
    print(f"m1 количество: {m1.get_count()}\n")

    # Создаем с определенным размером
    m5 = Money_task_2(123.45, size=10)
    print(f"m5 размер: {m5.size()}")  # 10
    print(f"m5 количество: {m5.get_count()}\n")

    # Тестируем изменение через индексацию
    m6 = Money_task_2(100.00)
    print(f"Начальное m6: {m6}")
    m6[0] = 5
    m6[1] = 0
    print(f"Измененное m6: {m6}")
