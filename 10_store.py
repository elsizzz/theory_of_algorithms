#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculate_store_inventory(goods_dict: dict, store_dict: dict) -> dict:
    """Рассчитывает общее количество и суммарную стоимость товаров на складе."""
    inventory_report = {}
    for good_name, code in goods_dict.items():
        batches = store_dict.get(code, [])
        total_quantity = sum(batch['quantity'] for batch in batches)
        total_cost = sum(batch['quantity'] * batch['price'] for batch in batches)
        inventory_report[good_name] = {
            'quantity': total_quantity,
            'cost': total_cost
        }
    return inventory_report


if __name__ == '__main__':
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    report = calculate_store_inventory(goods, store)
    for name, data in report.items():
        print(f"{name} - {data['quantity']} шт, стоимость {data['cost']} руб")