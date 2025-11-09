#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from money_package import Money_task_2


def test_initialization_from_int():
    # Тест инициализации из целого числа (в копейках)
    money = Money_task_2(12345)
    assert str(money) == "123 руб. 45 коп."
    assert money.to_kopecks() == 12345


def test_initialization_from_float():
    # Тест инициализации из числа с плавающей точкой
    money = Money_task_2(123.45)
    assert str(money) == "123 руб. 45 коп."
    assert money.to_kopecks() == 12345


def test_initialization_from_string():
    # Тест инициализации из строки
    money1 = Money_task_2("123.45")
    assert str(money1) == "123 руб. 45 коп."

    money2 = Money_task_2("100")
    assert str(money2) == "100 руб. 00 коп."


def test_initialization_from_list():
    # Тест инициализации из списка цифр
    money = Money_task_2([5, 4, 3, 2, 1])
    assert str(money) == "123 руб. 45 коп."


def test_size_methods():
    # Тест методов размера
    money_default = Money_task_2(100)
    assert money_default.size() == 100
    assert money_default.get_count() == 3  # 100.00 = 3 цифры

    money_custom = Money_task_2(100, size=50)
    assert money_custom.size() == 50


def test_indexing():
    money = Money_task_2(123.45)

    assert money[0] == 5
    assert money[1] == 4
    assert money[2] == 3
    assert money[3] == 2
    assert money[4] == 1

    money[0] = 9
    assert money[0] == 9
    assert str(money) == "123 руб. 49 коп."


def test_invalid_size():
    # Неверный размер
    with pytest.raises(ValueError):
        Money_task_2(100, size=1)

    with pytest.raises(ValueError):
        Money_task_2(100, size=101)


def test_invalid_value_type():
    # Тест неверного типа значения
    with pytest.raises(TypeError):
        Money_task_2(None)
