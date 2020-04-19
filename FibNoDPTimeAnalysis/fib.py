import time

def fib(n):
	if n == 0 or n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)

n = 35

start = time.time()
fib(n)
end = time.time()

print(end-start)
