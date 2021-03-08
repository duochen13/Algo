
"""
input: n: length of rod, price: a list of price with corresponding rod length
output: max profit
"""

# f(n): the max profit with the rod of length n
# f(n) = p[x] + f(n - x)
# f(0) = 0


def rodCuttingBottomUp(n, price):
    assert n < len(price)
    dp = [price[i] for i in range(n + 1)]
    for j in range(1, n + 1):
        for i in range(j):
            dp[j] = max(dp[j], dp[i] + dp[j - i])
    print(price)
    print(dp)
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


"""
Greedy does not work
ex: p = [0, 4, 7, ] corresponding length = [1,2,3]
    d = [0, 2, 2.3]
    n = 4
based on greedy stragegy, it will cut l=3, n-l=1, total price = 7+0 = 7
but 2 rods of length = 2, yields the profits 4 + 4 = 8
"""
def rodCuttingDensity(n, price):
    pass


"""
The revenue associated with a solution is now the sum of the prices of the pieces minus the costs of making the cuts.
"""
# f(n) = p[x] + f(n - x) + cost
def rodCuttingModified(n, price, cost=1):
    dp = [x for x in price]
    for i in range(1, n + 1):
        for j in range(i):
            print("dp[{}] = {}, dp[{}] - cost + dp[{}] = {}".format(i, dp[i], j, i - j, dp[i - j]))
            dp[i] = max(dp[i], dp[j] - cost + dp[i - j])
        print("===>dp[{}] = {}".format(i, dp[i]))
    print("cost:{}, price:{}".format(cost, price))
    print("dp:{}".format(dp))
    return dp[-1]


"""
The modified version of rodCutting algo with actual results
"""
def rodCuttingResults(n, price):
    dp = [[x, [i]] for i, x in enumerate(price)]
    for i in range(1, n + 1):
        for j in range(i):
            lastProfit, lastCoins = dp[i - j]
            if lastProfit + dp[j][0] > dp[i][0]:
                dp[i][0] = lastProfit + dp[j][0]
                dp[i][1] = lastCoins + [j]
    pass

price_0 = [0,1,5,8,9, 10,17,17,20,24,30]
answe_0 = [0,1,5,8,10,13,17,18,22,25,30]

#        0 1 2 3
price = [0,4,6,              8]
answe = [0,4,4+4-1,4+4+4-2]

assert rodCuttingModified(3, price) == 10
