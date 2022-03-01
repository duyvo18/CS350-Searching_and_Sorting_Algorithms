#include <iostream>
#include <algorithm>

int main()
{
	/*
	 * Read input size
	 */
	int input_size;
	std::cin >> input_size;

	/*
	 * Handle edge case
	 */
	if (input_size < 3)
	{
		std::cout << "NO";
		return 0;
	}

	/*
	 * Read input to array of segment lengths
	 */
	int *segment_lengths = new int[input_size];
	for (int i = 0; i < input_size; ++i)
	{
		std::cin >> segment_lengths[i];
	}

	/*
	 * Sort length array O(nlogn)
	 */
	std::sort(segment_lengths, segment_lengths + input_size);

	/*
	 * Given a < b < c in sorted array
	 *  -> b+c>a  & a+c>b due to ordering
	 *   therefore if a+b>c
	 *    -> a,b,c is non degenerate triangle
	 */
	for (int i = 0; i < input_size - 2; ++i)
	{
		if (segment_lengths[i] + segment_lengths[i + 1] > segment_lengths[i + 2])
		{
			std::cout << "YES";

			delete[] segment_lengths;
			return 0;
		}
	}

	/*
	 * Fall-through case
	 */
	std::cout << "NO";

	delete[] segment_lengths;
	return 0;
}
