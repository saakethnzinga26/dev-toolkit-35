def is_valid_input(value):
    if isinstance(value, int):
        return value > 0 and value < 1000
    elif isinstance(value, str):
        try:
            num = int(value)
            return num > 0 and num < 1000
        except ValueError:
            return False
    elif isinstance(value, float):
        return value > 0 and value < 1000 and value.is_integer()
    return False

def transform_data(val):
    if isinstance(val, str):
        val = int(val)
    return val * val + 5

def main():
    data = [5, -3, 42, "100", "abc", 3.0, 1500, "200", 7.5]
    results = []
    counter = 0
    while counter < len(data):
        item = data[counter]
        if is_valid_input(item):
            transformed = transform_data(item)
            results.append(transformed)
            if len(results) % 3 == 0:
                current_sum = sum(results)
                results.append(current_sum)
        counter += 1
    print("Processed results:", results)
    final = []
    for r in results:
        if r < 10000:
            final.append(r)
        else:
            final.append(r // 2)
    print("Final output:", final)

if __name__ == "__main__":
    main()