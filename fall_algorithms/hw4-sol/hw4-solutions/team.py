#!/usr/bin/env python3

__author__ = "Liang Huang"

from heapq import heapify, heapreplace

def _select(*lists):
    k = len(lists)
    n = len(lists[0])
    heap = [(a[0], i, 0) for i, a in enumerate(lists)]
    print("Heap  : ",heap)
    heapify(heap)
    print("AFTER HEAPIFY : ",heap)
    for _ in range(n):
        x, i, j = heap[0]
        yield x
        if j < n-1:
            heapreplace(heap, (lists[i][j+1], i, j+1))
            print("After replace : ",heap)

select = lambda *x: list(_select(*x))

if __name__ == "__main__":
    from random import randint
    import sys
    try:
        k, n = list(map(int, sys.argv[1:3]))
    except:
        k, n = 10, 2
    lists = [[1, 5, 7, 9], [0,4,8,10], [2,3,6,7]]
    print(lists)
    print(select(*lists))
