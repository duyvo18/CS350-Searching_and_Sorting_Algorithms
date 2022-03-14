#include <iostream>

int main()
{
    int n, max_dist;
    std::cin >> n >> max_dist;

    int *index_arr = new int[n];
    for (int i = 0; i < n; ++i)
        std::cin >> index_arr[i];
    
    long long ways = 0;
    int left = 0;
    for (int right = 0; right < n; ++right) {
        while (index_arr[right] - index_arr[left] > max_dist && left < right)
            ++left;
        
        long long tmp = right - left;
        ways += (long long)(tmp * (tmp - 1) / 2);
    }

    std::cout << ways;
}