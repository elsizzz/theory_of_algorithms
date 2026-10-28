#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def analyze_flora(garden_tuple: tuple, meadow_tuple: tuple) -> dict:
    """Выполняет теоретико-множественные операции над коллекциями растений."""
    garden_set = set(garden_tuple)
    meadow_set = set(meadow_tuple)
    return {
        'all_flowers': garden_set | meadow_set,
        'both_places': garden_set & meadow_set,
        'only_garden': garden_set - meadow_set,
        'only_meadow': meadow_set - garden_set,
    }


if __name__ == '__main__':
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

    results = analyze_flora(garden, meadow)
    print('Все виды цветов:', results['all_flowers'])
    print('Растут и там, и там:', results['both_places'])
    print('Только в саду:', results['only_garden'])
    print('Только на лугу:', results['only_meadow'])