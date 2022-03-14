from copy import deepcopy
import re

"""
    Create a list of tuple given a list and a constant element
"""
ListToTuple = lambda lst, idx: [(_, idx) for _ in lst]

"""
    Create a list of integer given a space seperated input
"""
SpaceSeperatedInputToList = lambda max_split: map(
    int, input().split(maxsplit=max_split)
)


def main():
    """
    dist_arr: List of (throw_dist, team_idx)
    """
    n = int(input())
    dist_arr = ListToTuple(SpaceSeperatedInputToList(max_split=n - 1), 0)

    m = int(input())
    dist_arr.extend(ListToTuple(SpaceSeperatedInputToList(max_split=m - 1), 1))

    dist_arr.sort(reverse=True)

    """
        The base case is limit distance = inf
        --> All throws are 2 points
    """
    max_point = [2 * n, 2 * m]
    curr_point = deepcopy(max_point)

    """
        Iteratively decrease the distance limit
        
        O(N)
        O(1)
    """
    for limit_dist in dist_arr:
        if limit_dist[1] == 0:
            curr_point[0] += 1
        else:
            curr_point[1] += 1

        '''
            Update max point if valid
            
            Note: Since the distance limit is decreasing
                  The result is both the max subtracted value
                  And the max point for Team 1
        '''
        if curr_point[0] - curr_point[1] >= max_point[0] - max_point[1]:
            max_point = deepcopy(curr_point)

    print(*max_point, sep=":")


if __name__ == "__main__":
    main()
