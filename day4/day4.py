from typing import List

def get_array_from_file():
    result = []
    with open('./day4/input.txt', 'r') as file:
        content = file.read()
        result = content.split('\n')
    return result

def get_formated_ranges(line: str) -> List[List[str]]:
    ranges = line.split(',')
    ranges = [ranges[0].split("-"), ranges[1].split("-")]
    return ranges

def get_sequence_from_range(range_input: List[str])->List[int]:
    return [int(range_input[0]), int(range_input[1])]

def is_in_range(seq_1: List[int], seq_2: List[int]) -> bool:
    return (seq_1[0] <= seq_2[0] and seq_1[1] >= seq_2[1]) or  (seq_2[0] <= seq_1[0] and seq_2[1] >= seq_1[1])

def is_overlaping(seq_1: List[int], seq_2: List[int]) -> bool:
    return (seq_2[1] >= seq_1[0] >= seq_2[0] or seq_1[1] >= seq_2[0] >= seq_1[0])

if __name__ == "__main__":
    r = get_array_from_file()
    total = 0
    total_2 = 0

    for i in r:
        formated_range = get_formated_ranges(i)
        seq_1, seq_2 = get_sequence_from_range(formated_range[0]), get_sequence_from_range(formated_range[1])
        if is_in_range(seq_1, seq_2):
            total += 1
        if is_overlaping(seq_1, seq_2):
            total_2 += 1
    print(total)
    print(total_2)

