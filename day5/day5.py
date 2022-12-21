piles = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: ""
}

def get_array_from_file():
    result = []
    with open('./day5/input.txt', 'r') as file:
        content = file.read()
        result = content.split('\n')
    return result

def get_first_part(file):
    for i, element in enumerate(file):
        if element[0:2] == " 1":
            print(i)
            return file[0:i], i

def get_second_part(file, index):
    return file[index+2:]

def initialise_data(first_part):
    for element in first_part:
        current_pile = 0
        for j in range(len(element)):
            if (j-1) % 4 == 0:
                current_pile += 1
                piles[current_pile] += element[j]

def sanitize_data(piles):
    for i in piles.keys():
        piles[i] = piles[i].replace(' ', '')
        piles[i] = piles[i][::-1]
    return piles

def move_crate(number: int, source: int, destination: int):
    for i in range(number):
        box_to_move = piles[source][-1:]
        piles[source] = piles[source][:-1]
        piles[destination] = piles[destination]+box_to_move

def move_crate_2(number: int, source: int, destination: int):
    box_to_move = piles[source][-number:]
    piles[source] = piles[source][:-number]
    piles[destination] = piles[destination]+box_to_move

def get_int_from_instructions(second_part):
    result = []
    for i in second_part:
        instruction = i.split()
        result.append([int(instruction[1]), int(instruction[3]), int(instruction[5])])
    return result


#SVFDLGLWV
if __name__ == '__main__':
    r = get_array_from_file()
    first_part, index = get_first_part(r)
    second_part = get_second_part(r, index)
    initialise_data(first_part)
    piles = sanitize_data(piles)
    instructions = get_int_from_instructions(second_part)
    for i in instructions:
        move_crate_2(i[0], i[1], i[2])
    print(piles)
