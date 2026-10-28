#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculate_list_songs_duration(songs_list: list, target_titles: list) -> float:
    """Суммирует длительность треков из списка по их названиям."""
    songs_map = dict(songs_list)
    total = sum(songs_map[title] for title in target_titles)
    return round(total, 3)


def calculate_dict_songs_duration(songs_dict: dict, target_titles: list) -> float:
    """Суммирует длительность треков из словаря по их названиям."""
    total = sum(songs_dict[title] for title in target_titles)
    return round(total, 3)


if __name__ == '__main__':
    violator_songs_list = [
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

    violator_songs_dict = {
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

    t1 = calculate_list_songs_duration(violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
    print(f'Три песни звучат {t1} минут')

    t2 = calculate_dict_songs_duration(violator_songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    print(f'А другие три песни звучат {t2} минут')