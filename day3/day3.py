import string
from typing import List

def get_array_from_file():
    result = []
    with open('./day3/input.txt', 'r') as file:
        content = file.read()
        result = content.split('\n')
    return result

    
def get_points(letter: str) -> int:
    if letter == None:
        return 0
    if letter.isupper():
        result = string.ascii_uppercase.index(letter)+1
        return result+26
    else:
        return string.ascii_lowercase.index(letter)+1

class Sack:
    def __init__(self, sack: str) -> None:
        self.f_comp = sack[0:(len(i)//2)]
        self.s_comp = sack[(len(i)//2):]
    
    def get_common_item(self) -> str:
        result = set()
        for i in self.f_comp:
            if i in self.s_comp:
                result.add(i)
        return result.pop()

class Sacks:
    def __init__(self, sacks: List[str]) -> None:
        self.sacks = sacks
        pass


    def get_badge(self):
        result = []
        for i in self.sacks[0]:
            if i in self.sacks[1] and i in self.sacks[2] and len(result)==0:
                result.append(i)
        if len(result) > 0:
            return result[0]
        return ""
    

    def __repr__(self) -> str:
        return "{list}, result : {result}, total: {total}".format(list=self.sacks, result=self.get_badge(), total=get_points(self.get_badge()))


if __name__ == "__main__":
    r = get_array_from_file()
    # first part
    first_total = 0
    for i in r:
        sack = Sack(i)
        common = sack.get_common_item()
        first_total += get_points(common)
    print("first_total: " + str(first_total))
    # second part
    r_2=[]
    for i in range(0, len(r), 3):
        sacks = r[i:i+3]
        r_2.append(sacks)
    test = [["vJrwpWtwJgWrhcsFMMfFFhFpasdf", "ajqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSLasdf", "aPmmdzqPrVvPwwTWBwgsdf"], ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFnsdf", "ttgJtRGJQctTZtZTsdf", "CrZsJsPPZsGzwwsLwLmpwMDwsdf"]]
    second_total = 0
    for i in r_2:
        sacks = Sacks(i)
        print(sacks)
        second_total += get_points(sacks.get_badge())
    print("second_total: " + str(second_total))
