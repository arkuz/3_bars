from data_loaders import load_from_JSON
from math import sqrt, pow


BARS_NONE_MSG = "List of bars is empty!"


def prepare_bars(bars):
    places = []
    for el in bars["features"]:
        current_el = el["properties"]["Attributes"]
        current_el_coord = el["geometry"]["coordinates"]
        current_place = {"name": current_el["Name"],
                         "places": current_el["SeatsCount"],
                         "longitude": current_el_coord[0],
                         "latitude": current_el_coord[1]}
        places.append(current_place)
    if not places:
        return None
    return places


def find_max_bar(bars):
    if bars is not None:
        current_el = bars[0]["places"]
        for el in bars:
            if el["places"] > current_el:
                current_el = el["places"]
                current_name = el["name"]
        print("""The bar "%s" has MAX seats places -  %s""" %
              (current_name, str(current_el)))
    else:
        print(BARS_NONE_MSG)


def find_max_bar_easy(bars):
    new_bars = []
    if bars is not None:
        for el in bars:
            new_bars.append(el["places"])
        max_bar = max(new_bars)
        print("MAX seats places - " + str(max_bar))
    else:
        print(BARS_NONE_MSG)


def find_min_bar_easy(bars):
    new_bars = []
    if bars is not None:
        for el in bars:
            new_bars.append(el["places"])
        min_bar = min(new_bars)
        print("MIN seats places - " + str(min_bar))
    else:
        print(BARS_NONE_MSG)


def find_min_bar(bars):
    if bars is not None:
        current_el = bars[0]["places"]
        for el in bars:
            if el["places"] < current_el:
                current_el = el["places"]
                current_name = el["name"]
        print("""The bar "%s" has MIN seats places - %s""" %
              (current_name, str(current_el)))
    else:
        print(BARS_NONE_MSG)


def distantion_between_points(x1, y1, x2, y2):
    return sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))


def find_near_bar(bars, longitude, latitude):
    if bars is not None:
        dist_bars = []
        for el in bars:
            dist = distantion_between_points(
                longitude, latitude, el["longitude"], el["latitude"])
            current_place = {"name": el["name"],
                             "places": el["places"],
                             "longitude": el["longitude"],
                             "latitude": el["latitude"],
                             "dist": dist}
            dist_bars.append(current_place)
        current_el = dist_bars[0]
        for el in dist_bars:
            if float(el["dist"]) < float(current_el["dist"]):
                current_el = el
        print("""The nearest bar is "%s" at a distance - %s""" %
              (current_el["name"], str(current_el["dist"])))
    else:
        print(BARS_NONE_MSG)


if __name__ == '__main__':
    try:
        longitude = float(input("Input your longitude: "))
        latitude = float(input("Input your latitude: "))

        json_bars = load_from_JSON("bars.json")
        prepared_bars = prepare_bars(json_bars)

        find_max_bar(prepared_bars)
        find_min_bar(prepared_bars)

        find_max_bar_easy(prepared_bars)
        find_min_bar_easy(prepared_bars)

        find_near_bar(prepared_bars, longitude, latitude)

    except ValueError:
        print("Incorrect input. Enter a number.")
