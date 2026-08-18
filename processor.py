import json

def process_data(data):
    if not isinstance(data, dict):
        raise TypeError('Expected a dictionary')
    return {k: v for k, v in data.items() if v is not None}


def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def transform_data(data):
    return {key.upper(): str(value) for key, value in data.items()}


def validate_data(data):
    if not isinstance(data, dict):
        return False
    return all(isinstance(key, str) and key for key in data.keys())


def main():
    sample_data = {'name': 'Alice', 'age': 30, 'city': None}
    processed = process_data(sample_data)
    print(f'Processed Data: {processed}')  
    save_to_file(processed, 'output.json')
    loaded_data = load_from_file('output.json')
    transformed = transform_data(loaded_data)
    print(f'Transformed Data: {transformed}')


if __name__ == '__main__':
    main()