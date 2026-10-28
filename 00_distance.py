#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculate_distances(sites: dict) -> dict:
    """Вычисляет расстояния между городами на координатной сетке."""
    distances = {}
    for city1, (x1, y1) in sites.items():
        distances[city1] = {}
        for city2, (x2, y2) in sites.items():
            if city1 != city2:
                dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = round(dist, 2)
    return distances


if __name__ == '__main__':
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    result = calculate_distances(sites)
    print(result)