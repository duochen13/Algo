

import collections

def playground1(nums):
    """
    Find odd number of zero digits
    :param nums: list of int
    :return: int
    """

    res = 0
    for num in nums:
        num = str(num)
        zeros = collections.Counter(num)['0']
        if zeros % 2:
            res += 1
    return res

def playground2(a, ss):
    """
    :param a: list of string
    :param ss: list of string
    """
    memo = set()
    for i in range(len(a)):
        tmp = a[i]
        memo.add(tmp)
        for j in range(i + 1, len(a)):
            tmp += a[j]
            memo.add(tmp)
    print(memo)
    for s in ss:
        if s not in memo:
            return False
    return True



if __name__ == '__main__':
    # nums = [10,100,4000, 10400]
    # res = playground1(nums)
    # print(res)

    a = ["apple", "pie", "pineapple"]
    s = ["applepie", "pineapplepie", "pie"]
    res = playground2(a, s)
    print(res)