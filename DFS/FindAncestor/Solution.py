from collections import defaultdict

def findStartAndEndLocations(pairs):
  # construct graph
  nodes = set()
  topDownMemo = defaultdict(list)
  bottomUpMemo = defaultdict(list)
  for start, end in pairs:
    nodes.add(start)
    topDownMemo[start].append(end)
    bottomUpMemo[end].append(start)

  # print("topDownMemo:{}".format(topDownMemo))
  # print("bottomUpMemo:{}".format(bottomUpMemo))

  # find start nodes
  starters = []
  for node in nodes:
    if not node in bottomUpMemo:
      starters.append(node)

  res = defaultdict(set)
  for startNode in starters:
    tmpSet = set()
    dfs(startNode, topDownMemo, tmpSet)
    res[startNode] = tmpSet

  for startNode in sorted(starters):
    print("{}: ".format(startNode), end='')
    for endNode in sorted(res[startNode]):
      print("{} ".format(endNode), end='')
    print('')


def dfs(node, topDownMemo, tmpSet):
  if not topDownMemo[node]:
    tmpSet.add(node)
    return
  for childNode in topDownMemo[node]:
    dfs(childNode, topDownMemo, tmpSet)
      

pairs = [['A','B'],
['A','C'],
['B','K'],
['C','K'],
['E','L'],
['F','G'],
['J','M'],
['E','F'],
['G','H'],
['G','I']]

# findStartAndEndLocations(pairs)


pairs = [[14,1],
[14,2],
[1,3],
[2,4],
[3,7],
[4,8],
[5,4],
[5,10]]

# {1: [14], 
# 2: [14], 
# 3: [1], 
# 4: [2, 5], 
# 7: [3], 
# 8: [4], 
# 10: [5]}

# f(3,4) 
# 3->1->14

# 4->2->14

class FindChild:

	def __init__(self, pairs):
		self.memo = defaultdict(list)
		for parent, child in pairs:
			self.memo[child].append(parent)
		print(self.memo)
		self.commonNode = None

	def dfs(self, node, ancestors):
		# base case
		if node in ancestors:
			self.commonNode = node
			return
		ancestors.add(node)
		for n in self.memo[node]:
			self.dfs(n, ancestors)

	def commonAncestor(self, node1, node2):
		ancestors = set()
		self.dfs(node1, ancestors)
		self.dfs(node2, ancestors)
		return self.commonNode


fc = FindChild(pairs)
res = fc.commonAncestor(3,4)
print(res)

