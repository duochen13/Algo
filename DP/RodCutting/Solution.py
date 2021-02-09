
"""
input: n: length of rod, price: a list of price with corresponding rod length
output: max profit
"""


def rodCuttingBottomUp(n, price):
    assert n < len(price)
    dp = [price[i] for i in range(n + 1)]
    for j in range(1, n + 1):
        for i in range(j):
            dp[j] = max(dp[j], dp[i] + dp[j - i])
    return dp[-1]


def rodCuttingTopDown(n, price):
    memo = {}
    memo[0], memo[1] = price[0], price[1]
    def helper(n, price, memo):
        if n in memo:
            # print("memo[{}] = {}".format(n, memo[n]))
            return memo[n]
        if n < 0:
            return 0
        # print("n:{}".format(n))
        res = price[n]
        for i in range(1, n):
            # print("n:{}, n - i:{}".format(n, n - i))
            res = max(res, price[i] + helper(n - i, price, memo))
        memo[n] = res
        return res
    return helper(n, price, memo)


price = [0,1,5,8,9, 10,17,17,20,24,30]
answe = [0,1,5,8,10,13,17,18,22,25,30]

for n in range(len(price)):
    res = rodCuttingTopDown(n, price)
    assert res == answe[n]


