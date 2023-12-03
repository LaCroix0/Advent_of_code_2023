import re
from functools import reduce

list_of_colors = ['red', 'blue', 'green']
pattern = r'[1-9][0-9]'
pattern2 = r'[1-9]'
counter_dict = {}


def part_1(row: str):
    checker = True
    row = row[row.index(':') + 1:]
    row = row.strip('\n')
    row = row.split(';')
    out = []
    max_r = 0
    max_b = 0
    max_g = 0
    for l in row:
        l = l.strip(' ')
        out.append(l.split(','))
    for li in out:
        for li2 in li:
            li2 = li2.replace(' ', '')
            if re.match(pattern2, li2):
                match (li2[1]):
                    case 'r':
                        if int(li2[0]) > max_r:
                            max_r = int(li2[0])
                    case 'b':
                        if int(li2[0]) > max_b:
                            max_b = int(li2[0])
                    case 'g':
                        if int(li2[0]) > max_g:
                            max_g = int(li2[0])
            if re.match(pattern, li2):
                match (li2[2]):
                    case 'r':
                        if int(li2[:2]) > 12:
                            checker = False
                        if int(li2[:2]) > max_r:
                            max_r = int(li2[:2])
                    case 'b':
                        if int(li2[:2]) > 14:
                            checker = False
                        if int(li2[:2]) > max_b:
                            max_b = int(li2[:2])
                    case 'g':
                        if int(li2[:2]) > 13:
                            checker = False
                        if int(li2[:2]) > max_g:
                            max_g = int(li2[:2])
    # part_1
    # return checker

    # part_2
    return (max_r * max_g * max_b)



with open('input.txt', 'r') as file:
    res = []
    # part_1
    # for index, line in enumerate(file, start=1):
    #     if part_1(line):
    #         res.append(index)
    # print(f'result for part 1: {int(reduce(lambda a, b: a + b, res))}')
    # part_2
    for line in file:
        res.append(part_1(line))

    print(f'result for part 2: {int(reduce(lambda a, b: a + b, res))}')

file.close()
