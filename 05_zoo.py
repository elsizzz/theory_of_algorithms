#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def modify_zoo(initial_zoo: list, birds: list) -> list:
    """Выполняет модификацию списка животных согласно заданию."""
    zoo = initial_zoo.copy()
    # 1. Посадить медведя между львом и кенгуру
    zoo.insert(1, 'bear')
    # 2. Добавить птиц в последние клетки
    zoo.extend(birds)
    # 3. Убрать слона
    if 'elephant' in zoo:
        zoo.remove('elephant')
    return zoo


def get_animal_cage_number(zoo: list, animal_name: str) -> int:
    """Возвращает номер клетки (1-индексированный)."""
    return zoo.index(animal_name) + 1


if __name__ == '__main__':
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']

    updated_zoo = modify_zoo(zoo, birds)
    print(updated_zoo)
    print(f'Лев сидит в клетке номер {get_animal_cage_number(updated_zoo, "lion")}')
    print(f'Жаворонок сидит в клетке номер {get_animal_cage_number(updated_zoo, "lark")}')