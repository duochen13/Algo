# 1, O(n) = k * C(n, k)
def dfs(candidates, start, elements, target, res):

    if target < 0:
        return
    if target == 0:
        # print(list(elements))
        res.append(list(elements))
        return
    
    for i in range(start, len(candidates)):
        num = candidates[i]
        elements.append(num)
        dfs(candidates, i, elements, target - num, res)
        elements.pop()


def combinationSumRecursion(candidates, target):

    res = []
    
    dfs(candidates, start=0, elements=[], target, res)
    
    return res


# 2
def combinationSumIteration(candidates, target):
    
    res = []
    stack = [([], 0, target)]
    
    while stack:
        elements, start, target = stack.pop()
        # base case
        if target == 0:
            print(list(elements))
            res.append(list(elements))
            continue
        # dfs
        for i in range(start, len(candidates)):
            num = candidates[i]
            if target - num < 0:
                continue
            # elements.append(num)
            stack.append((elements + [num], i, target - num))
            # elements.pop()
    
    return res