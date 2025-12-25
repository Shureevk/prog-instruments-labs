import csv
from checksum import calculate_checksum, serialize_result
from consts import *


def load_data(file_path: str, delimiter: str = CSV_DELIMITER):
    with open(file_path, "r", encoding=FILE_ENCODING, newline="") as file:
        reader = csv.reader(file, delimiter=delimiter)
        return list(reader)


def validate_row(row: list[str], patterns: list[re.Pattern]) -> bool:
    if len(row) != len(patterns):
        return False

    return all(
        pattern.fullmatch(value.strip())
        for pattern, value in zip(patterns, row)
    )


def find_invalid_rows(data: list[list[str]], patterns: list[re.Pattern]) -> list[int]:
    invalid_rows = []

    for index, row in enumerate(data[1:], start=0):  # пропускаем заголовок
        if not validate_row(row, patterns):
            invalid_rows.append(index)

    return invalid_rows


def main():
    print("CSV Validation Script")

    data = load_data(DEFAULT_FILE_PATH)
    patterns = get_validation_patterns()

    invalid_rows = find_invalid_rows(data, patterns)
    print("Invalid rows:", len(invalid_rows))

    checksum_value = calculate_checksum(invalid_rows)
    serialize_result(DEFAULT_VARIANT, checksum_value)

    print("Checksum:", checksum_value)
    print(f"Result saved to result.json (variant {DEFAULT_VARIANT})")


if __name__ == "__main__":
    main()
