import json


def save_data(data, filename):
    with open(f'data/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_data(filename):
    with open(f'data/{filename}.json') as json_file:
        data = json.load(json_file)
    return data