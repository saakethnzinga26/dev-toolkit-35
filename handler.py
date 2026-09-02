import re
from collections import defaultdict

def process_inputs(input_list):
    processed = []
    i = 0
    stats = defaultdict(int)
    while i < len(input_list):
        current_input = input_list[i]
        i += 1
        text = str(current_input).strip()
        if len(text) < 5:
            stats['too_short'] += 1
            continue
        if len(text) > 100:
            stats['too_long'] += 1
            continue
        if not re.match(r'^[a-zA-Z0-9 ]+$', text):
            stats['invalid_chars'] += 1
            continue
        transformed = text.replace(' ', '_')[::-1].upper()
        processed.append(transformed)
        stats['valid'] += 1
    return processed, dict(stats)

def execute_handler(data):
    result, stats = process_inputs(data)
    return {"processed_items": result, "validation_stats": stats}

def get_summary(handler_output):
    items = handler_output["processed_items"]
    if not items:
        return "No valid items"
    return f"First: {items[0]}, Total: {len(items)}"

if __name__ == "__main__":
    sample = ["good data here", "bad!", "ok data 123", "too short", "valid entry with spaces", "another@invalid", "this is a longer but valid input for testing"]
    output = execute_handler(sample)
    print(output)
    print(get_summary(output))
