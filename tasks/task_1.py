#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from class_money import Money

if __name__ == "__main__":

    print("\nСоздание через конструктор:")
    try:
        money1 = Money(100, 5)
        money1.display()
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Создание объектов
    m1 = Money(100, 5)
    m2 = Money(100, 3)
    m3 = Money(500, 2)

    print("Демонстрация перегруженных операторов:")
    print(f"m1 = {m1}")
    print(f"m2 = {m2}")
    print(f"m3 = {m3}\n")

    print("Арифметические операции:")
    print(f"m1 + m2 = {m1 + m2}")
    print(f"m1 - m2 = {m1 - m2}")
    print(f"m1 * 2 = {m1 * 2}")
    print(f"2 * m1 = {2 * m1}\n")

    print("Операции сравнения:")
    print(f"m1 == m2: {m1 == m2}")
    print(f"m1 > m2: {m1 > m2}")
    print(f"m1 < m3: {m1 < m3}")
    print(f"m1 <= m2: {m1 <= m2}")
    print(f"m1 >= m2: {m1 >= m2}\n")

    print("Преобразование типов:")
    print(f"int(m1): {int(m1)}")
    print(f"float(m1): {float(m1)}")
    print(f"bool(m1): {bool(m1)}\n")
