import json


def load_from_JSON(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            decoded_json = json.load(file)
            return decoded_json
        except json.decoder.JSONDecodeError:
            return None


if __name__ == '__main__':
    pass
