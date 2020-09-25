

"""
input:
2 -> 10
4 -> 100   (2 zeros)
7 -> 0111
8 -> 1000
16 -> 10000 (4 zeros)

requirements: 
number of zeros is even && starting with 1

"""


def powerOfFour(num):
    singleOne = not (num >> 1) & num
    numZeros = len(bin(num)[3:]) # or while loop
    return singleOne and not numZeros % 2


assert powerOfFour(4) == True
assert powerOfFour(16) == True
assert powerOfFour(8) == False
assert powerOfFour(1) == True