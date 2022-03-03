'''
    Read size input
'''
input_size = int(input())


'''
    Read badges inputs
'''
badges = []
for elem in [int(elem_input) for elem_input in input().split(' ', input_size - 1)]:
    badges.append(elem)

    
'''
    Create and calculate offset frequency list
        offset_freqency_list[i] = number of occurrence of the ith smallest badge
        
    Time: O(n)
    Space: O(n)
'''
min_value_offset = min(badges)
badges_variance = max(badges) - min_value_offset

compensated_freq_lst_size = input_size*2 - min_value_offset + 1
compensated_freq_lst = [0] * compensated_freq_lst_size

for idx in range(input_size):
    elem_value = badges[idx]
    
    compensated_idx = elem_value - min_value_offset
    compensated_freq_lst[compensated_idx] += 1


'''
    Normalize offset frequency list
        If a value A has > 1 occurrence
            Shift all excessive unit of A frequency to A+1
                That is, add 1 to ALL excessive occurrences of A (called "offset")
                Then, increase the frequency of A+1 by "offset" to compensate
                    -> "offset" is also the number of coin needed to spent
    Time: O(n)
'''
coin_needed = 0
for idx in range(compensated_freq_lst_size - 1):
    if compensated_freq_lst[idx] > 1:
        offset = compensated_freq_lst[idx] - 1
        
        compensated_freq_lst[idx + 1] += offset
        compensated_freq_lst[idx] -= offset
        
        coin_needed += offset


print(coin_needed)