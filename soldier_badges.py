input_size = int(input())

coin_needed = 0
badges = []
for elem in [int(elem_input) for elem_input in input().split(' ', input_size - 1)]:
    while elem in badges:
        elem += 1
        coin_needed += 1
    badges.append(elem)

print(coin_needed)