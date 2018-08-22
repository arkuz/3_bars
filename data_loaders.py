import json


def load_from_JSON(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            json_file = json.load(file)
            return json_file
        except json.decoder.JSONDecodeError:
            return None


if __name__ == '__main__':
    pass
