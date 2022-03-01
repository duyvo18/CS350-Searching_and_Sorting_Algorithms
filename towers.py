'''
    Ignore size input
'''
int(input())


'''
    bar_heights_freq = {input_value: value_frequency}
'''
bar_heights_freq = {}

elem_inputs = input().split()
for input in elem_inputs:
    elem = int(input)
    bar_heights_freq[elem] = bar_heights_freq.get(elem, 0) + 1


'''
    Number of bars = Number of elements in non-duplicated dictionary
    O(1)
'''
total_bars = len(bar_heights_freq)

'''
    Highest bar height = Largest frequency value
    O(n)
'''
highest_bar_height = max(bar_heights_freq.values())


print(f"{highest_bar_height} {total_bars}")