import re
from dataclasses import dataclass
from typing import List

@dataclass
class ValidationResult:
    is_valid: bool
    reason: str

def check_format(value: str) -> ValidationResult:
    if not value:
        return ValidationResult(False, "empty")
    if not re.match(r"^[a-z0-9]+$", value.lower()):
        return ValidationResult(False, "invalid chars")
    if len(value) < 2:
        return ValidationResult(False, "too short")
    return ValidationResult(True, "ok")

def transform_value(value: str) -> str:
    return value.upper() + "_PROCESSED"

def main_processing_loop(raw_inputs: List[str]) -> List[str]:
    validated_outputs: List[str] = []
    for raw in raw_inputs:
        validation = check_format(raw)
        if validation.is_valid:
            transformed = transform_value(raw)
            validated_outputs.append(transformed)
        else:
            validated_outputs.append(f"INVALID_{validation.reason.upper()}")
    final_results = []
    pos = 0
    while pos < len(validated_outputs):
        item = validated_outputs[pos]
        if not item.startswith("INVALID"):
            final_results.append(item)
        pos += 1
    return final_results

if __name__ == "__main__":
    test_data = ["hello", "123abc", "Bad!", "", "ok", "a"]
    result = main_processing_loop(test_data)
    print(result)