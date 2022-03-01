#include <iostream>
#include <algorithm>

int main() {
	/*
	 * Read the input
	 */
	int n;
	std::cin >> n;
	
	int* a = new int[n];
	for (int i = 0; i < n; ++i) {
		std::cin >> a[i];
	}

	/*
	 * Sorting (nlogn)
	 */
	std::sort(a, a + n);

	/*
	 * Given a < b < c in sorted array
	 *  -> b+c>a  & a+c>b due to ordering
	 *  therefore if a+b>c
	 *   -> a,b,c is non degenerate triangle
	 */
	for (int i = 0; i < n - 2; ++i) {
		if (a[i] + a[i+1] > a[i+2]) {
			std::cout << "YES";
			
			delete[] a;
			return 0;
		}
	}
	
	std::cout << "NO";

	delete[] a;
	return 0;
}
