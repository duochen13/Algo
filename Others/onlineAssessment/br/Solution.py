import collections


def coinChangeBottomUp(coins, N):
    """
    dp[amount]: min number of coins sum to amount
    """
    dp = [float('inf') for _ in range(N + 1)]
    dp[0] = 0
    for i in range(N + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    print("dp: ", dp)

    return dp[N] if dp[N] != float('inf') else -1



def dfs(coins, amount, tmp, memo, currents):
    """
    coins: list of int
    amount: int
    tmp: int
    """
    # base case
    if amount < 0:
        return -1
    if amount == 0:
        print("amount: ", amount, ", currents: ", currents)
        memo[amount] = tmp
        return tmp
    # look up
    if amount in memo:
        return memo[amount]
    res = float('inf')
    for coin in coins:
        if amount - coin < 0:
            continue
        currents.append(coin)
        res = min(res, dfs(coins, amount - coin, tmp + 1, memo, currents))
        currents.pop()
    # store for future look-up
    memo[amount] = res
    return res


def coinChangeTopDown(coins, N):
    """
    coins: list of int
    N: int
    """
    memo = collections.defaultdict(int)
    currents = []
    res = dfs(coins, N, 0, memo, currents)
    return res if res != float('inf') else -1



if __name__ == "__main__":
    coins = [3, 2, 5]
    N = 11
    res = coinChangeTopDown(coins, N)

    print(res)
