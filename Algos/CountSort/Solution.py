
"""
input: [6,0,2,0,1,3,4,6,1,3,2]

This is the array we sort

   +---+---+---+---+---+---+---+---+---+---+---+
A: | 6 | 0 | 2 | 0 | 1 | 3 | 4 | 6 | 1 | 3 | 2 |
   +---+---+---+---+---+---+---+---+---+---+---+

We build an array of counts:

     0   1   2   3   4   5   6
   +---+---+---+---+---+---+---+
C: | 2 | 2 | 2 | 2 | 1 | 0 | 2 |
   +---+---+---+---+---+---+---+

The number of elements before each

     0   1   2   3   4   5   6
   +---+---+---+---+---+---+----+
C: | 2 | 4 | 6 | 8 | 9 | 9 | 11 |
   +---+---+---+---+---+---+----+


ref: https://ita.skanev.com/08/02/01.html
"""

def countSort(A):
    upperbound = max(A)
    C = [0 for _ in range(upperbound + 1)]
    for a in A:
        C[a] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # we will recover C at line 42
    B = [0 for _ in range(len(A) + 1)]
    for i in range(len(A) - 1, -1, -1): # if we do i in [1...len(A)], work properly, but not stable(same elements)
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
    # recover C
    return B[1:]


"""
Q: Describe an algorithm that, given nn integers in the range 00 to kk, preprocesses its input and then answers any query about how many of the nn integers fall into a range [a..b][a..b] in \O(1)O(1) time. Your algorithm should use \Theta(n+k)Θ(n+k) preprocessing time.
"""

def apply(A, k, a, b):
    C = [0 for _ in range(k + 1)]
    for num in A:
        C[num] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    assert a <= b
    if a == 0:
        return C[b]
    return C[b] - C[a - 1]


assert countSort(A=[1, 1, 2, 2, 4, 5, 7]) == [1, 1, 2, 2, 4, 5, 7]
assert countSort(A=[6,0,2,0,1,3,4,6,1,3,2]) == [0,0,1,1,2,2,3,3,4,6,6]
assert apply(A=[2,0,1,1,4,3], k=4, a=1, b=3) == 4
assert apply(A=[2,0,1,1,4,3], k=4, a=0, b=2) == 4
