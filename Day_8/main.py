with open('input.txt', 'r') as file:
    # linked_list = LinkedList()
    directions = file.readline()
    directions_dictionary = {}
    for line in file:
        if line.find('='):
            line = line.strip().replace(' ', '')
            line = line.split('=')
            if len(line) > 1:
                directions_dictionary[line[0]] = line[1]
    # Part 1
    counter = 0
    curr = 'AAA'
    res = []

    while curr != 'ZZZ':
        for char in directions:
            left = directions_dictionary[curr].strip('()').split(',')[0]
            right = directions_dictionary[curr].strip('()').split(',')[1]
            if char == 'L':
                curr = left
                res.append(1)
            if char == 'R':
                curr = right
                res.append(1)
    print(f'part 1 solution: {len(res)}')

    # Part 2
