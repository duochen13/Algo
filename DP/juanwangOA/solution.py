# 2.medium, N: HP, M: [0, M], K: number of swings
# http://kriszhang.com/shaizi_google/
import math, decimal

def helper(n, m, hp, memo):
    # base case: kill monster with 1 hit (dmg delat 'm' greater than 'hp')
    if n == 1:
        return 1 if hp >= 0 and hp <= m else 0
    key = "{}:{}".format(n, hp)
    # look up pre-calculated value
    if key in memo:
        return memo[key]
    res = 0 
    for dmg in range(m + 1):
        res += helper(n - 1, m, hp - dmg, memo)
    # store the new calculated value in hashtable for future look up
    memo[key] = res
    return res

def probGreaterThan(n, m, x):
    # n: number of time hitting monster, m: attack power,  x: the damage dealt
    res = 0
    memo = {}
    while x <= m * n:
        res += helper(n, m, x, memo)
        x += 1
    return res

def beatMonster(n, m, k):
    numberOfCombs = probGreaterThan(k, m, n)
    if numberOfCombs == 0:
        return decimal.Decimal('0.00000')
    # get total number of combinations, when hit monster 'k' times
    totalCombs = math.pow(m + 1, k)
    res = numberOfCombs / totalCombs
    return round(res, 5)


assert beatMonster(n=2,m=1,k=3) == 0.5
assert beatMonster(n=3,m=1,k=6) == 0.65625
# print(beatMonster(n=10,m=5,k=2))
# print(beatMonster(n=100,m=5,k=2))
# print(beatMonster(n=1000,m=1000,k=1000))
# print(beatMonster(n=4,m=1,k=6))
# print(beatMonster(n=20,m=3,k=10))
# print(beatMonster(n=99,m=66,k=33))
