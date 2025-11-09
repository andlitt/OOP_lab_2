#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money_task_2:
    MAX_SIZE = 100

    def __init__(self, value=0, size=None):
        if size is None:
            size = self.MAX_SIZE
        if size < 2 or size > self.MAX_SIZE:
            raise ValueError(f"Размер должен быть от 2 до {self.MAX_SIZE}")

        self._size = size
        self._digits = [0] * size

        # Конвертируем значение в копейки и сохраняем цифры в обратном порядке
        if isinstance(value, (int, float)):
            total_kopecks = (
                int(round(value * 100)) if isinstance(value, float) else value
            )
        elif isinstance(value, str):
            if "." in value:
                parts = value.split(".")
                rub = parts[0] if parts[0] else "0"
                kop = parts[1].ljust(2, "0")[:2] if len(parts) > 1 else "00"
                total_kopecks = int(rub) * 100 + int(kop)
            else:
                total_kopecks = int(value) * 100
        elif isinstance(value, list):
            total_kopecks = 0
            for i, digit in enumerate(value):
                if i >= size:
                    break
                total_kopecks += digit * (10**i)
        else:
            raise TypeError("Неподдерживаемый тип значения")

        # Сохраняем цифры в обратном порядке
        num = total_kopecks
        for i in range(size):
            if num == 0:
                break
            self._digits[i] = num % 10
            num //= 10

        self._count = self._compute_count()

    def _compute_count(self):
        count = 2
        for i in range(self._size - 1, -1, -1):
            if self._digits[i] != 0:
                count = i + 1
                break
        return count

    def size(self):
        return self._size

    def get_count(self):
        return self._count

    def to_kopecks(self):
        total = 0
        for i in range(self._size):
            total += self._digits[i] * (10**i)
        return total

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._digits[index]
        raise IndexError("Индекс вне диапазона")

    def __setitem__(self, index, value):
        if 0 <= index < self._size:
            if not (0 <= value <= 9):
                raise ValueError("Цифра должна быть от 0 до 9")
            self._digits[index] = value
            self._count = self._compute_count()
        else:
            raise IndexError("Индекс вне диапазона")

    def __str__(self):
        # Извлекаем рубли и копейки
        kopecks = self._digits[1] * 10 + self._digits[0] if self._size >= 2 else 0

        ruble_digits = []
        for i in range(2, self._count):
            ruble_digits.append(str(self._digits[i]))

        if ruble_digits:
            rubles = "".join(reversed(ruble_digits))
        else:
            rubles = "0"

        return f"{rubles} руб. {kopecks:02d} коп."

    def __repr__(self):
        return f"Money({self.to_kopecks() / 100:.2f}, размер={self._size})"
