#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculate_expression() -> int:
    """Возвращает результат математического выражения для ряда чисел 1 2 3 4 5."""
    return ((1 + 2) * 3 - 4) * 5


if __name__ == '__main__':
    result = calculate_expression()
    print(result)