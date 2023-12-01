from functools import reduce

# directory of nums translated into words
num_dict: dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# function for resolving day 1 part 2
def day_1_part_2(query):
    tmp = '*' * len(query)
    counter = 0
    for char in query:
        if char.isdigit():
            tmp = tmp[:counter] + char + tmp[counter:]
        counter += 1
    for key in num_dict.keys():
        v = find_occurence(query, key)
        for value in v:
            string_list = list(tmp)
            string_list[value] = str(num_dict[key])
            tmp = ''.join(string_list)

    return tmp.replace('*', '')


# generator for finding indexes of all occurences of nums in words
def find_occurence(query, substring):
    start = 0
    while True:
        start = query.find(substring, start)
        if start == -1:
            return
        yield start
        start += len(substring)


with open('Day_1/input.txt', 'r') as file:
    res = []
    for line in file:
        res.append(day_1_part_2(line))

    file.close()
nums = []

# converting strings to ints and adding them together
for item in res:
    if len(item) > 1:
        tmp = str(item[0]) + str(item[-1])
    else:
        tmp = f'{item}{item}'
    nums.append(int(tmp))

print(f'Wynik: {reduce(lambda a, b: a + b, nums, 0)}')
