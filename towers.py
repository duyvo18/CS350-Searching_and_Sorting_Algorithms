n = int(input())

# dict = {input_value: value_frequency}
dict = {}
elemInputs = input().split()
for input in elemInputs:
	elem = int(input)
	dict[elem] = dict.get(elem, 0) + 1

total_bars = len(dict) # O(1)
highest_bar_height = max(dict.values()) # O(n)

print(f'{highest_bar_height} {total_bars}')

