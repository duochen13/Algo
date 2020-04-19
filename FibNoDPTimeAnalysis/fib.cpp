#include <iostream>
#include <time.h>

using namespace std;

int fib(int n) {
	if (n == 0 || n == 1)
		return 1;
	return fib(n - 1) + fib(n - 2);
}

int main() {
	int res;

	clock_t start = clock();
	fib(35);
	clock_t end = clock();	

	cout << (double)(end - start)/CLOCKS_PER_SEC << endl;
}
