def get_array_from_file():
    result = []
    with open('./day6/input.txt', 'r') as file:
        content = file.read()
        result = content.split('\n')
    return result

def get_location_in_string(code, window_size):
    for i in range(len(code)):
        window = code[i:i+window_size]
        if len(set(window)) == window_size:
            return i+window_size
    return -1


if __name__ == "__main__":
    r = get_array_from_file()
    code = r[0]
    result = get_location_in_string(code, 4)
    result_2 = get_location_in_string(code, 14)
    print(result)
    print(result_2)
