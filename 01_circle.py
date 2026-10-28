#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_circle_area(radius: float, pi: float = 3.1415926) -> float:
    """Вычисляет площадь круга с округлением до 4 знаков."""
    return round(pi * (radius ** 2), 4)


def is_point_inside_circle(point: tuple, radius: float) -> bool:
    """Проверяет, лежит ли точка внутри круга с центром в (0, 0)."""
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    return distance <= radius


if __name__ == '__main__':
    radius = 42
    print(get_circle_area(radius))

    point_1 = (23, 34)
    print(is_point_inside_circle(point_1, radius))

    point_2 = (30, 30)
    print(is_point_inside_circle(point_2, radius))