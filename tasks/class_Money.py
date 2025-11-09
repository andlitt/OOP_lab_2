#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    VALID_NOMINALS = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]

    def __init__(self, first, second):
        if not self.check_nominal(first):
            raise ValueError(
                f"Номинал {first} не поддерживается. Допустимые:"
                f"{self.VALID_NOMINALS}"
            )
        if second < 1:
            raise ValueError(f"Количество {second} должно быть не менее 1")
        self.first = first  # номинал
        self.second = second  # количество

    # Проверка корректности номинала
    def check_nominal(self, value):
        return value in self.VALID_NOMINALS

    # Арифметические операции
    def __add__(self, other):
        # Сложение денег (только с одинаковым номиналом)
        if isinstance(other, Money):
            if self.first != other.first:
                raise ValueError("Сложение возможно только для одинаковых номиналов")
            return Money(self.first, self.second + other.second)
        return NotImplemented

    def __sub__(self, other):
        # Вычитание денег (только с одинаковым номиналом)
        if isinstance(other, Money):
            if self.first != other.first:
                raise ValueError("Вычитание возможно только для одинаковых номиналов")
            if self.second < other.second:
                raise ValueError("Недостаточно купюр для вычитания")
            return Money(self.first, self.second - other.second)
        return NotImplemented

    def __mul__(self, other):
        # Умножение на число
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Множитель не может быть отрицательным")
            return Money(self.first, int(self.second * other))
        return NotImplemented

    def __rmul__(self, other):
        # Умножение числа на деньги (справа)
        return self.__mul__(other)

    def __truediv__(self, other):
        # Деление на число
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Делитель должен быть положительным")
            return Money(self.first, max(1, int(self.second / other)))
        return NotImplemented

    # Операции сравнения
    def __eq__(self, other):
        # Проверка равенства (по общей сумме)
        if isinstance(other, Money):
            return self.summa() == other.summa()
        return False

    def __lt__(self, other):
        # Сравнение меньше (по общей сумме)
        if isinstance(other, Money):
            return self.summa() < other.summa()
        return False

    def __le__(self, other):
        # Сравнение меньше или равно (по общей сумме)
        if isinstance(other, Money):
            return self.summa() <= other.summa()
        return False

    def __gt__(self, other):
        # Сравнение больше (по общей сумме)
        if isinstance(other, Money):
            return self.summa() > other.summa()
        return False

    def __ge__(self, other):
        # Сравнение больше или равно (по общей сумме)
        if isinstance(other, Money):
            return self.summa() >= other.summa()
        return False

    # Составные присваивания
    def __iadd__(self, other):
        # += оператор
        if isinstance(other, Money):
            if self.first != other.first:
                raise ValueError("Сложение возможно только для одинаковых номиналов")
            self.second += other.second
            return self
        return NotImplemented

    def __isub__(self, other):
        # -= оператор
        if isinstance(other, Money):
            if self.first != other.first:
                raise ValueError("Вычитание возможно только для одинаковых номиналов")
            if self.second < other.second:
                raise ValueError("Недостаточно купюр для вычитания")
            self.second -= other.second
            return self
        return NotImplemented

    def __imul__(self, other):
        # *= оператор
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Множитель не может быть отрицательным")
            self.second = int(self.second * other)
            return self
        return NotImplemented

    def __itruediv__(self, other):
        # /= оператор
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Делитель должен быть положительным")
            self.second = max(1, int(self.second / other))
            return self
        return NotImplemented

    # Преобразование типов
    def __int__(self):
        # Преобразование в целое число (общая сумма)
        return self.summa()

    def __float__(self):
        # Преобразование в вещественное число (общая сумма)
        return float(self.summa())

    def __bool__(self):
        # Логическое преобразование (True если есть купюры)
        return self.second > 0

    # Строковые представления
    def __str__(self):
        # Пользовательское строковое представление
        return f"{self.second} × {self.first} руб. = {self.summa()} руб."

    def __repr__(self):
        # Строковое представление для отладки
        return f"Money({self.first}, {self.second})"

    # Индексация и контейнерные операции
    def __getitem__(self, index):
        # Доступ к номиналу и количеству по индексу
        if index == 0:
            return self.first
        elif index == 1:
            return self.second
        elif index == 2:
            return self.summa()
        else:
            raise IndexError("Индекс должен быть 0, 1 или 2")

    def __setitem__(self, index, value):
        # Изменение номинала или количества по индексу
        if index == 0:
            if not self.check_nominal(value):
                raise ValueError(f"Номинал {value} не поддерживается")
            self.first = value
        elif index == 1:
            if value < 1:
                raise ValueError(f"Количество {value} должно быть не менее 1")
            self.second = value
        else:
            raise IndexError("Индекс должен быть 0 или 1")

    def __len__(self):
        # Количество параметров (номинал, количество, сумма)
        return 3

    def __contains__(self, item):
        # Проверка наличия номинала в допустимых номиналах
        return item in self.VALID_NOMINALS

    # Ввод с клавиатуры
    def read(self):
        try:
            first = int(input("Введите номинал купюры: "))
            second = int(input("Введите количество купюр: "))

            if not self.check_nominal(first):
                print(f"Ошибка: Номинал {first} не поддерживается")
                print(f"Допустимые номиналы: {self.VALID_NOMINALS}")
                return False

            if second < 1:
                print(f"Ошибка: Количество {second} должно быть не менее 1")
                return False

            self.first = first
            self.second = second
            return True

        except ValueError:
            print("Ошибка: Введите числовые значения")
            return False

    # Вывод на экран
    def display(self):
        print(f"Номинал: {self.first} руб.")
        print(f"Количество: {self.second} шт.")
        print(f"Общая сумма: {self.summa()} руб.")

    # Вычисление суммы
    def summa(self):
        return self.first * self.second


def make_money(first, second):
    try:
        return Money(first, second)
    except ValueError as e:
        raise ValueError(f"Ошибка создания объекта Money: {e}")
