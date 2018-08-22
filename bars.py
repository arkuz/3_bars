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
        longitude = float(input("Input your longitude: "))
        latitude = float(input("Input your latitude: "))
    except ValueError:
        print("Incorrect input. Enter a number.")
        exit()

    bars = load_from_JSON(bars_file_path)
    if bars is None:
        print("Load error. JSON file is incorrect.")
        exit()

    max_bar = find_max_bar(bars)
    min_bar = find_min_bar(bars)
    near_bar = find_near_bar(bars, longitude, latitude)

    print("The biggest bar is '{0}' - {1} places.".format(
        max_bar["properties"]["Attributes"]["Name"],
        max_bar["properties"]["Attributes"]["SeatsCount"]))

    print("The smalest bar is '{0}' - {1} places.".format(
        min_bar["properties"]["Attributes"]["Name"],
        min_bar["properties"]["Attributes"]["SeatsCount"]))

    print("The nearest bar is '{0}', distantion - {1:.2f}.".format(
        near_bar["properties"]["Attributes"]["Name"],
        near_bar["distantion"]))
