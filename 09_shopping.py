#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_top_two_cheapest_shops(shops_data: dict) -> dict:
    """Автоматически находит по 2 магазина с минимальными ценами для каждого товара."""
    prices_by_product = {}
    for shop_name, items in shops_data.items():
        for item in items:
            p_name = item['name']
            p_price = item['price']
            if p_name not in prices_by_product:
                prices_by_product[p_name] = []
            prices_by_product[p_name].append({'shop': shop_name, 'price': p_price})

    cheapest_sweets = {}
    for p_name, shop_list in prices_by_product.items():
        sorted_shops = sorted(shop_list, key=lambda x: x['price'])
        cheapest_sweets[p_name] = sorted_shops[:2]

    return cheapest_sweets


if __name__ == '__main__':
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

    sweets = find_top_two_cheapest_shops(shops)
    print(sweets)