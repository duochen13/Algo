import math
import sys

def is_sqrt(n):
	x = int(math.sqrt(n))
	return x * x == n

def play(nums, N):
	memo = [1 for _ in range(len(nums) + 1)]
	for i in range(len(nums)):
		memo[i + 1] = nums[i] * memo[i]
	print(memo)
	cur_len = float('-inf')
	l = r = 0
	for i in range(len(memo)):
		for j in range(i):
			assert memo[i] % memo[j] == 0
			tmp = int(memo[i] / memo[j])
			if not is_sqrt(tmp):
				continue
			# update result
			if i - j > cur_len:
				cur_len = i - j
				l = j
				r = i
	return (l + 1, r) if cur_len != float('-inf') else -1


first = True
N = -1
for line in sys.stdin:
	if first:
		N = int(line)
		first = False
	else:
		if line == '\n':
			break
		nums = [int(x) for x in line.split(' ')]
		# res can either be -1 or (l, r)
		res = play(nums, N)
		print(res)



# first = True
# N = -1
# for line in lines:
# 	if first:
# 		N = int(line)
# 		first = False
# 	else:
# 		line = line.strip()
# 		nums = [int(x) for x in line.split(' ')]
# 		# res can either be -1 or (l, r)
# 		res = play(nums, N)
# 		print(res)

