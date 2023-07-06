# Implementation of a max-heap from an unordered array

def max_heapify(A, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    
def build_max_heap(A):
    n = int((len(A) // 2) - 1)
    for i in range(n, -1, -1):
        max_heapify(A,i)