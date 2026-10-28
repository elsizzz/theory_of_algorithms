#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_family_data():
    """Возвращает информацию о семье и их росте."""
    my_family = ['Мама', 'Папа', 'Я', 'Бабушка']
    my_family_height = [
        ['Мама', 168],
        ['Папа', 182],
        ['Я', 175],
        ['Бабушка', 160],
    ]
    return my_family, my_family_height


def get_member_height(family_height: list, name: str) -> int:
    """Возвращает рост конкретного члена семьи."""
    for member, height in family_height:
        if member == name:
            return height
    raise ValueError(f'Член семьи {name} не найден')


def get_total_family_height(family_height: list) -> int:
    """Рассчитывает суммарный рост членов семьи."""
    return sum(member[1] for member in family_height)


if __name__ == '__main__':
    family, family_height = get_family_data()
    father_height = get_member_height(family_height, 'Папа')
    print(f'Рост отца - {father_height} см')

    total_height = get_total_family_height(family_height)
    print(f'Общий рост моей семьи - {total_height} см')