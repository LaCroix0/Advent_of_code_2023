# from functools import reduce
#
#
# # part 1 solution
# def part_1(row: str):
#     row = row[row.index(':') + 1:]
#     row = row.strip('\n ')
#     row = row.split('|')
#     winning_numbers = row[0].split(' ')
#     winning_numbers = [int(x) for x in winning_numbers if x != '']
#     my_numbers = row[1].split(' ')
#     my_numbers = [int(x) for x in my_numbers if x != '']
#     correct = []
#     for num in my_numbers:
#         if num in winning_numbers:
#             correct.append(num)
#     # print(f'my numbers : {my_numbers}')
#     # print(f'winning numbers : {correct}')
#     # print(f'matching numbers : {correct}')
#     out = 2 ** (len(correct) - 1) if len(correct) > 0 else 0
#     return out
#
#
# # part 2 solution
# def part_2(row: str):
#     row = row[row.index(':') + 1:]
#     row = row.strip('\n ')
#     row = row.split('|')
#     winning_numbers = row[0].split(' ')
#     winning_numbers = [int(x) for x in winning_numbers if x != '']
#     my_numbers = row[1].split(' ')
#     my_numbers = [int(x) for x in my_numbers if x != '']
#     correct = []
#     for num in my_numbers:
#         if num in winning_numbers:
#             correct.append(num)
#     return len(correct)
#
#
# with open('input.txt', 'r') as file:
#     res = []
#     cards_dics = {}
#     for line in file:
#         res.append(part_1(line))
#
#     print(f'part 1 solution: {int(reduce(lambda a, b: a + b, res))}')
#     print(f'part 2 solution: ')
