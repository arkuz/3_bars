import json


def load_from_JSON(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    pass
