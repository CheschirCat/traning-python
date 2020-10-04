#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distances = dict()

Moscow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']


Moscow_London = round((((Moscow[0] - London[0]) ** 2 + ((Moscow[1] - London[1]) ** 2)) ** 0.5), 2)
Paris_Moscow = round((((Moscow[0] - Paris[0]) ** 2 + ((Moscow[1] - Paris[1]) ** 2)) ** 0.5), 2)
London_Paris = round((((London[0] - Paris[0]) ** 2 + ((London[1] - Paris[1]) ** 2)) ** 0.5), 2)

distances['Moscow'] = {}
distances['Moscow'] ['London'] = Moscow_London
distances['Moscow'] ['Paris'] = Paris_Moscow

distances['London'] = {}
distances['London'] ['Moscow'] = Moscow_London
distances['London'] ['Paris'] = London_Paris

distances['Paris'] = {}
distances['Paris'] ['London'] = London_Paris
distances['Paris'] ['Moscow'] = Paris_Moscow

pprint(distances)