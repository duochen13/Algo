import sys
import time

def fib(n):
	if n == 0 or n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)

n = int(sys.argv[1])

start = time.time()
fib(n)
end = time.time()

print("py: ", (end-start) * 1000, "ms")
