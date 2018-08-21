from data_loaders import load_from_JSON
from math import sqrt, pow
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path of JSON file")
args = parser.parse_args()
bars_file_path = os.path.abspath(args.file)


def get_find_key():
    return lambda key: key["properties"]["Attributes"]["SeatsCount"]


def find_max_bar(bars):
    return max(bars["features"], key=get_find_key())


def find_min_bar(bars):
    return min(bars["features"], key=get_find_key())


def calc_distantion_between_points(x1, y1, x2, y2):
    return sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))


def find_near_bar(bars, longitude, latitude):
    for bar in bars["features"]:
        x1 = longitude
        y1 = latitude
        x2 = bar["geometry"]["coordinates"][0]
        y2 = bar["geometry"]["coordinates"][1]
        bar["distantion"] = calc_distantion_between_points(x1, y1, x2, y2)
    return min(bars["features"], key=lambda x: x["distantion"])

if __name__ == '__main__':
    try:
        print(bars_file_path)
        #longitude = float(input("Input your longitude: "))
        #latitude = float(input("Input your latitude: "))

        longitude = 5
        latitude = 5

        bars = load_from_JSON(bars_file_path)

        print(find_max_bar(bars))
        print(find_min_bar(bars))
        print(find_near_bar(bars, longitude, latitude)["distantion"] )

    except ValueError:
        print("Incorrect input. Enter a number.")
