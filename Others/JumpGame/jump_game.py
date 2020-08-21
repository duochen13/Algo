import time
import random

# Index:  0 1 2 3 4
# Input: [2,3,1,1,4]
#.    i:  0
#.    s:  1
#.    e:  0
#maxend:  2

# Output: 2
N = 750
nums = [random.randint(0, 9) for _ in range(N)]
# nums = [2,3,1,1,4,2,5,1,3,4,5,7,2,1,3,1,0,0,2,1]
print("nums: ", nums)

def jump(nums):
	s = e = res = 0
	while e + 1 < len(nums):
		res += 1
		max_end = float('-inf')
		for i in range(s, e + 1):
			max_end = max(max_end, i + nums[i])
		s = e + 1
		e = max_end
	return res

start = time.time()
result = jump(nums)
end = time.time()

print(end - start)
