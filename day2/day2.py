def get_array_from_file():
    result = []
    with open('input.txt', 'r') as file:
        content = file.read()
        result = content.split('\n')
    return result

class Match:
    def __init__(self, round: str, half: int = 1):
        self.half = half
        self.round = round
        if len(round) == 3:
            self.p_1 = round[0]
            self.p_2 = round[2]
        if half == 2:
            self.first_p_2 = self.p_2
            self.transform_input()

        else:
            raise ValueError("invalid round input: {round}".format(round=round))
    
    def transform_input(self):
        if self.first_p_2=="X":
            if self.p_1=="A":self.p_2="Z"
            if self.p_1=="B":self.p_2="X"
            if self.p_1=="C":self.p_2="Y"
        if self.first_p_2=="Y":
            if self.p_1=="A":self.p_2="X"
            if self.p_1=="B":self.p_2="Y"
            if self.p_1=="C":self.p_2="Z"
        if self.first_p_2=="Z":
            if self.p_1=="A":self.p_2="Y"
            if self.p_1=="B":self.p_2="Z"
            if self.p_1=="C":self.p_2="X"


    
    def get_p2_choice_score(self) -> int:
        score = {"X":1, "Y":2, "Z":3}
        return score[self.p_2]
    
    def get_match_score(self) -> int:
        match = self.p_1 + self.p_2
        winning_drawing_score = {
            "AY":6,
            "AX":3,
            "BZ":6,
            "BY":3,
            "CX":6,
            "CZ":3
        }
        if match in winning_drawing_score:
            return winning_drawing_score[match]
        else:
            return 0
    
    def get_total(self):
        return self.get_p2_choice_score() + self.get_match_score()
    
    def print(self):
        print("match: {match}, result: {total},".format(match=self.p_1 + self.p_2, total=self.get_total()))



"""
A: Rock
B: Paper
C: Scissors
X: Rock
Y: Paper
Z: Scissors
"""


if __name__ == "__main__":
    r = get_array_from_file()
    matches = [Match(i, 2) for i in r]
    total = 0
    for i in matches:
        i.print()
        total += i.get_total()
    
    print(total)