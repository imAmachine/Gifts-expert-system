import json


def load_json(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(e)


def json_update(path, data):
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(e)