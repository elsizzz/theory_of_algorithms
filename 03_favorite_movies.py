#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def extract_movies(movies_str: str) -> dict:
    """Извлекает названия фильмов с помощью срезов строки."""
    return {
        'first': movies_str[:10],
        'last': movies_str[-15:],
        'second': movies_str[12:25],
        'second_from_end': movies_str[-22:-17]
    }


if __name__ == '__main__':
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    movies = extract_movies(my_favorite_movies)
    print(movies['first'])
    print(movies['last'])
    print(movies['second'])
    print(movies['second_from_end'])