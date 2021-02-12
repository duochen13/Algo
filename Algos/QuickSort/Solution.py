
def partitionTwo(A, l, r):
    """loop invariant:
    A[l:i] <= x
    A[i:j] >= x
    A[j:] unknown
    """
    last = len(A) - 1
    x = A[last]
    i = l - 1
    for j in range(l, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        print("A:{}".format(A))
    A[i + 1], A[last] = A[last], A[i + 1]
    print("A:{}".format(A))
    return i + 1


def quickSortTwo(A, l, r):
    if l + 1 >= r:
        return
    pivot = partitionTwo(A, l, r)
    print(pivot)
    assert 0
    quickSort(A, l, pivot)
    quickSort(A, pivot + 1, r)


def partitionThree(A, p, r):
    last = len(A) - 1
    x = A[last]
    i = p - 1
    # invariant: A[:i] is less than A[pivot]
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[last] = A[last], A[i + 1]


def quickSortThree(A, p, r): # inclusive
    if p >= r:
        return
    q, t = partitionThree(A, p, r)
    quickSortThree(A, p, q)
    quickSortThree(A, q + 1, t)
    quickSortThree(A, t + 1, r)


A = [13,19,3,5,12,8,7,4,21,2,6,11]
quickSort(A, 0, len(A))

