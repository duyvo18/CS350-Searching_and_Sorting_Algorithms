#include <iostream>
#include <algorithm>

int main()
{
    /*
     * Read the input
     */
    int input_size;
    std::cin >> input_size;

    int *test_index_arr = new int[input_size];
    int *end = test_index_arr + input_size;
    for (int i = 0; i < input_size; ++i)
    {
        std::cin >> test_index_arr[i];
    }


    /*
     * Sort the array
     * 
     * Time: O(nlogn)
     */
    std::sort(test_index_arr, end);


    /*
     * Iterate from index 1 to find the first unused index
     *
     * Time: O(n)
     * Space: O(1)
     */
    int next_test_index = 1;
    int *current_test_index = test_index_arr;

    while (next_test_index == *current_test_index && current_test_index != end)
    {
        // std::cout << "Res: " << next_test_index << "\n"
        //           << "Cur: " << *current_test_index << "\n"
        //           << "Bool: " << (next_test_index == *current_test_index) << "\n\n";
        ++next_test_index;
        ++current_test_index;
    }

    std::cout << next_test_index;

    delete[] test_index_arr;
    return 0;
}