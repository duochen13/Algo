
"""
input: n: length of rod, price: a list of price with corresponding rod length
output: max profit
"""


def rodCutting(n, price):
    assert n < len(price)
    dp = [price[i] for i in range(n + 1)]
    for j in range(1, n + 1):
        for i in range(j):
            dp[j] = max(dp[j], dp[i] + dp[j - i])
    return dp[-1]


price = [0,1,5,8,9, 10,17,17,20,24,30]
answe = [0,1,5,8,10,13,17,18,22,25,30]

for n in range(len(price)):
    res = rodCutting(n, price)
    assert res == answe[n]


