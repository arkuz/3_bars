import json


def load_from_JSON(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            file_object = json.load(file)
            return file_object
        except json.decoder.JSONDecodeError:
            return None


if __name__ == '__main__':
    pass
