# import numpy as np
# import re
#
# reg = r'/(?=\D)(?!\.)/g'
#
# def part_1(row: str):
#     signs_indexes = []
#     for char in row:
#         if re.match(reg, char):
#             signs_indexes.append(row.find(char))
#
#
# with open('input.txt', 'r') as file:
#     for line in file:
#         print(part_1(line))
