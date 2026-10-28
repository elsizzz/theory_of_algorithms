#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import sys
from pathlib import Path

# Гарантируем, что текущая папка находится в путях импорта Python
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Динамический импорт модулей
mod_00 = importlib.import_module("00_distance")
mod_01 = importlib.import_module("01_circle")
mod_02 = importlib.import_module("02_operations")
mod_03 = importlib.import_module("03_favorite_movies")
mod_04 = importlib.import_module("04_my_family")
mod_05 = importlib.import_module("05_zoo")
mod_06 = importlib.import_module("06_songs_list")
mod_07 = importlib.import_module("07_secret")
mod_08 = importlib.import_module("08_garden")
mod_09 = importlib.import_module("09_shopping")
mod_10 = importlib.import_module("10_store")


def run_task_00():
    print("\n--- Задание 00: Расстояния между городами ---")
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    distances = mod_00.calculate_distances(sites)
    for city1, targets in distances.items():
        print(f"{city1}:")
        for city2, dist in targets.items():
            print(f"  -> {city2}: {dist}")


def run_task_01():
    print("\n--- Задание 01: Площадь круга и координаты точек ---")
    radius = 42
    print(f"Площадь круга (R={radius}): {mod_01.get_circle_area(radius)}")
    
    p1 = (23, 34)
    p2 = (30, 30)
    print(f"Точка {p1} внутри круга: {mod_01.is_point_inside_circle(p1, radius)}")
    print(f"Точка {p2} внутри круга: {mod_01.is_point_inside_circle(p2, radius)}")


def run_task_02():
    print("\n--- Задание 02: Расстановка арифметических операций ---")
    print(f"Выражение ((1 + 2) * 3 - 4) * 5 = {mod_02.calculate_expression()}")


def run_task_03():
    print("\n--- Задание 03: Срезы названий фильмов ---")
    raw_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    movies = mod_03.extract_movies(raw_movies)
    print(f"Первый: {movies['first']}")
    print(f"Последний: {movies['last']}")
    print(f"Второй: {movies['second']}")
    print(f"Второй с конца: {movies['second_from_end']}")


def run_task_04():
    print("\n--- Задание 04: Рост членов семьи ---")
    _, family_h = mod_04.get_family_data()
    father_h = mod_04.get_member_height(family_h, 'Папа')
    total_h = mod_04.get_total_family_height(family_h)
    print(f"Рост отца: {father_h} см")
    print(f"Общий рост семьи: {total_h} см")


def run_task_05():
    print("\n--- Задание 05: Животные в зоопарке ---")
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    updated_zoo = mod_05.modify_zoo(zoo, birds)
    print(f"Итоговый зоопарк: {updated_zoo}")
    print(f"Клетка льва (lion): №{mod_05.get_animal_cage_number(updated_zoo, 'lion')}")
    print(f"Клетка жаворонка (lark): №{mod_05.get_animal_cage_number(updated_zoo, 'lark')}")


def run_task_06():
    print("\n--- Задание 06: Длительность песен Depeche Mode ---")
    songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }
    t1 = mod_06.calculate_list_songs_duration(songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
    t2 = mod_06.calculate_dict_songs_duration(songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    print(f"Три песни из списка звучат: {t1} минут")
    print(f"Три песни из словаря звучат: {t2} минут")


def run_task_07():
    print("\n--- Задание 07: Расшифровка секретного сообщения ---")
    secret = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    print(f"Результат: \"{mod_07.decrypt_message(secret)}\"")


def run_task_08():
    print("\n--- Задание 08: Множества цветов сада и луга ---")
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    res = mod_08.analyze_flora(garden, meadow)
    print(f"Все виды цветов: {res['all_flowers']}")
    print(f"Растут и там, и там: {res['both_places']}")
    print(f"Только в саду: {res['only_garden']}")
    print(f"Только на лугу: {res['only_meadow']}")


def run_task_09():
    print("\n--- Задание 09: Минимальные цены в магазинах ---")
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    }
    sweets = mod_09.find_top_two_cheapest_shops(shops)
    for product, offers in sweets.items():
        print(f"{product.capitalize()}:")
        for offer in offers:
            print(f"  - {offer['shop']}: {offer['price']} руб")


def run_task_10():
    print("\n--- Задание 10: Складской учет ---")
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }
    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
        '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
        '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
    }
    report = mod_10.calculate_store_inventory(goods, store)
    for name, data in report.items():
        print(f"{name} - {data['quantity']} шт, стоимость {data['cost']} руб")


TASKS = {
    "0": ("Расстояния между городами", run_task_00),
    "1": ("Площадь круга и точки", run_task_01),
    "2": ("Расстановка операций (число 25)", run_task_02),
    "3": ("Срезы фильмов", run_task_03),
    "4": ("Семья и рост", run_task_04),
    "5": ("Зоопарк", run_task_05),
    "6": ("Песни Depeche Mode", run_task_06),
    "7": ("Секретное сообщение", run_task_07),
    "8": ("Цветы сада и луга (set)", run_task_08),
    "9": ("Минимальные цены в магазинах", run_task_09),
    "10": ("Складской учет", run_task_10),
}


def run_all():
    print("\n" + "=" * 50)
    print("ЗАПУСК ВСЕХ ЗАДАНИЙ ЛАБОРАТОРНОЙ РАБОТЫ №1")
    print("=" * 50)
    for key in sorted(TASKS.keys(), key=lambda x: int(x)):
        title, func = TASKS[key]
        func()
    print("\n" + "=" * 50)


def show_menu():
    print("\n" + "=" * 45)
    print("      МЕНЮ ВЫБОРА ЗАДАНИЯ (ЛАБ. РАБОТА №1)")
    print("=" * 45)
    for key in sorted(TASKS.keys(), key=lambda x: int(x)):
        title, _ = TASKS[key]
        print(f" [{key:>2}] {title}")
    print(" [all] Выполнить все задания подряд")
    print(" [ q ] Выход")
    print("=" * 45)


def main():
    while True:
        show_menu()
        choice = input("Введите номер задания для запуска: ").strip().lower()

        if choice in ('q', 'exit', 'quit', 'й'):
            print("\nЗавершение работы программы.")
            break
        elif choice == 'all':
            run_all()
        elif choice in TASKS:
            TASKS[choice][1]()
        else:
            print("\n[!] Неверный ввод. Пожалуйста, укажите число от 0 до 10, 'all' или 'q'.")

        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == '__main__':
    main()