# with open('input.txt', 'r') as file:
#     t = ''
#     r = ''
#     for index, line in enumerate(file):
#         if index == 0:
#             t = line
#         if index == 1:
#             r = line
#     t = t[t.index(':') + 1:]
#     r = r[r.index(':') + 1:]
#     times = t.split()
#     records = r.split()
#
#     times_p2 = t.replace(' ', '')
#     records_p2 = r.replace(' ', '')
#
# tr_dict = {times[i]: records[i] for i in range(len(times))}
#
#
# def p1(T, R):
#     tmp_t = T
#     possible_times = []
#     for time in range(0, tmp_t):
#         d = time * (T - time)
#         if d > R:
#             possible_times.append(1)
#     return len(possible_times)
#
#
# out = 1
# for k, v in tr_dict.items():
#     out *= p1(int(k), int(v))
# print(f'part 1 answer: {out}')
# print(f'part 2 answer: {p1(int(times_p2), int(records_p2))}')
