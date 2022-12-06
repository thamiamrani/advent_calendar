def get_array_from_file():
    result = []
    with open('input.txt', 'r') as file:
        content = file.read()
        result = content.split('\n')
    return result

def get_sums(input_array):
    current_sum = 0
    sums = []
    for i in input_array:
        if i == "":
            sums.append(current_sum)
            current_sum = 0
            continue
        current_sum += int(i)
    return sums

def get_answer(list_sums):
    sorted_list = sorted(list_sums, reverse=True)
    top_3 = [sorted_list[0], sorted_list[1], sorted_list[2]]
    return """
            Max : {max} \n
            Top3 : {top_3}\n
            sum of Top3: {sum_of_top3}
           """.format(max=sorted_list[0], top_3=top_3, sum_of_top3=sum(top_3))

if __name__ == '__main__':
    r = get_array_from_file()
    final_r = get_sums(r)
    print(get_answer(final_r))