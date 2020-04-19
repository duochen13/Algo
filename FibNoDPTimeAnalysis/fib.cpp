#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

int fib(int n) {
	if (n == 0 || n == 1)
		return 1;
	return fib(n - 1) + fib(n - 2);
}

int main(int argc, char *argv[]) {
	int res;
	int N = atoi(argv[1]);
	clock_t start = clock();
	fib(N);
	clock_t end = clock();	

	cout << "c++: " << 1000 * (double)(end - start)/CLOCKS_PER_SEC << "ms" << endl;
}
