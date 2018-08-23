from data_loaders import load_from_JSON
from math import sqrt, pow
import argparse
import os
import sys


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Path of JSON file')
    return parser


def get_seats_count():
    return lambda bar: bar['properties']['Attributes']['SeatsCount']


def get_distantion(longitude, latitude):
    return lambda dist: calc_distantion_between_points(
        longitude,
        latitude,
        float(dist['geometry']['coordinates'][0]),
        float(dist['geometry']['coordinates'][1]))


def find_max_bar(bars):
    return max(bars, key=get_seats_count())


def find_min_bar(bars):
    return min(bars, key=get_seats_count())


def calc_distantion_between_points(x1, y1, x2, y2):
    return sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))


def find_near_bar(bars, longitude, latitude):
    return min(bars, key=get_distantion(longitude, latitude))


def print_bar_info(bar, description_text=''):
    print('{0} bar is \'{1}\' - {2} places.'.format(
        description_text,
        bar['properties']['Attributes']['Name'],
        bar['properties']['Attributes']['SeatsCount']))


if __name__ == '__main__':
    try:
        longitude = float(input('Input your longitude: '))
        latitude = float(input('Input your latitude: '))
    except ValueError:
        sys.exit('Incorrect input. Enter a number.')

    parser = create_arg_parser()
    args = parser.parse_args()
    bars_file_path = os.path.abspath(args.file)

    bars = load_from_JSON(bars_file_path)
    if bars is None:
        sys.exit('Load error. JSON file is incorrect.')

    bars_features = bars['features']
    max_bar = find_max_bar(bars_features)
    min_bar = find_min_bar(bars_features)
    near_bar = find_near_bar(bars_features, longitude, latitude)

    print_bar_info(max_bar, 'The biggest')
    print_bar_info(min_bar, 'The smalest')
    print_bar_info(near_bar, 'The nearest')
