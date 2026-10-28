#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import pytest

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


def test_00_distance():
    sites = {'A': (0, 0), 'B': (3, 4)}
    res = mod_00.calculate_distances(sites)
    assert res['A']['B'] == 5.0
    assert res['B']['A'] == 5.0


def test_01_circle_area_and_points():
    assert mod_01.get_circle_area(10) == 314.1593
    # Точка (0, 42) лежит на границе
    assert mod_01.is_point_inside_circle((0, 42), 42) is True
    # Точка (30, 30) -> sqrt(1800) ≈ 42.42 > 42
    assert mod_01.is_point_inside_circle((30, 30), 42) is False


def test_02_operations():
    assert mod_02.calculate_expression() == 25


def test_03_movies():
    s = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    res = mod_03.extract_movies(s)
    assert res['first'] == 'Терминатор'
    assert res['second'] == 'Пятый элемент'
    assert res['second_from_end'] == 'Чужие'
    assert res['last'] == 'Назад в будущее'


def test_04_family():
    _, heights = mod_04.get_family_data()
    assert mod_04.get_member_height(heights, 'Папа') == 182
    assert mod_04.get_total_family_height(heights) == 168 + 182 + 175 + 160
    with pytest.raises(ValueError):
        mod_04.get_member_height(heights, 'Неизвестный')


def test_05_zoo():
    initial = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    updated = mod_05.modify_zoo(initial, birds)
    assert updated == ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    assert mod_05.get_animal_cage_number(updated, 'lion') == 1
    assert mod_05.get_animal_cage_number(updated, 'lark') == 7


def test_06_songs():
    songs_l = [['Song1', 3.5], ['Song2', 4.55], ['Song3', 2.005]]
    songs_d = {'Song1': 3.5, 'Song2': 4.55, 'Song3': 2.005}
    assert mod_06.calculate_list_songs_duration(songs_l, ['Song1', 'Song2']) == 8.05
    assert mod_06.calculate_dict_songs_duration(songs_d, ['Song2', 'Song3']) == 6.555


def test_07_decrypt():
    secret = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    assert mod_07.decrypt_message(secret) == 'в бане веник дороже денег'


def test_08_garden():
    g = ('роза', 'ромашка')
    m = ('ромашка', 'клевер')
    res = mod_08.analyze_flora(g, m)
    assert res['both_places'] == {'ромашка'}
    assert res['only_garden'] == {'роза'}
    assert res['only_meadow'] == {'клевер'}


def test_09_cheapest_shops():
    shops = {
        'shop1': [{'name': 'яблоко', 'price': 100}],
        'shop2': [{'name': 'яблоко', 'price': 80}],
        'shop3': [{'name': 'яблоко', 'price': 90}],
    }
    res = mod_09.find_top_two_cheapest_shops(shops)
    assert len(res['яблоко']) == 2
    assert res['яблоко'][0]['shop'] == 'shop2'
    assert res['яблоко'][1]['shop'] == 'shop3'


def test_10_store():
    goods = {'Лампа': '12345'}
    store = {'12345': [{'quantity': 2, 'price': 100}, {'quantity': 3, 'price': 200}]}
    rep = mod_10.calculate_store_inventory(goods, store)
    assert rep['Лампа']['quantity'] == 5
    assert rep['Лампа']['cost'] == 800