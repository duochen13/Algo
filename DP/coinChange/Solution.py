
"""
All you need to know about coin change
input: N: moeny, coins = [1,5,7]
output: boolean
others: Can repeatly use coins
"""

# f(n): can make change with quanity of money n
# base: f(i) = True for i in coins
# relation: f(n) = f(n - i)
def coinChangeBoolean(N, coins):
    assert N >= coins[-1]
    dp = [False for _ in range(N + 1)]
    dp[0] = True
    for d in coins:
        dp[d] = True
    for i in range(N + 1):
        for d in coins:
            if i - d >= 0 and dp[i - d]:
                dp[i] = True
    print("post dp:{}".format(dp))
    return dp[-1]


# output: min number of coins needed
# f(n): minimum number of coins to form quanity n
# f(n) = min(f(n), 1 + f(n - d))
def coinChangeInt(N, coins):
    dp = [float('inf') for _ in range(N + 1)]
    dp[0] = 0
    for d in coins:
        dp[d] = 1
    for i in range(N + 1):
        for d in coins:
            if i - d >= 0 and dp[i - d] != float('inf'):
                dp[i] = min(dp[i], dp[i - d] + 1)
    return dp[-1]


coins = [4,5,10]
print("coins: {}".format(coins))
for n in range(10, 22):
    res = coinChangeInt(n, coins)
    print("N:{}, #coins:{}".format(n, res))


print(res)

