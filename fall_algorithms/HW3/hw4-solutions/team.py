#!/usr/bin/env python3

__author__ = "Liang Huang"

from heapq import heapify, heapreplace
from random import randint

# modified qselect, return the sublist of top n smallest elements
def qselect(a, n): 
    idx = randint(0, len(a)-1)
    pivot = a[idx]
    a[0], a[idx] = a[idx], a[0]
    left = [x for x in a if x < pivot]
    remaining = (n - 1) - len(left)
    if remaining < 0:
        return qselect(left, n)
    elif remaining == 0:
        return left + [pivot]
    else:
        right = [x for x in a[1:] if x > pivot] 
        return left + [pivot] + qselect(right, remaining)

def _select(*lists):
    k = len(lists)
    n = len(lists[0])
    heap = [(a[0], i, 0) for i, a in enumerate(lists)]
    
    # when k >> n, you can prune down to n using quick select
    # this is asymptotically faster (O(k+k+nlogn) vs. O(k+nlogk))
    # but in practice not always the case 
    if use_qselect: 
        heap = qselect(heap, n)
        #assert len(heap) == n
        
    heapify(heap)
    for _ in range(n):
        x, i, j = heap[0]
        yield x
        if j < n-1:
            heapreplace(heap, (lists[i][j+1], i, j+1))

select = lambda *x: list(_select(*x))

if __name__ == "__main__":
    import time
    import sys
    try:
        k, n = list(map(int, sys.argv[1:3]))
    except:
        k, n = 10, 2
    lists = [sorted([randint(0, 100*k) for _ in range(n)]) for _ in range(k)]
    #print(lists)
    start_time = time.time()
    use_qselect = False
    results = select(*lists)    
    print("time: %.5f" % (time.time() - start_time))
    print(results)
    start_time = time.time()
    use_qselect = True
    results = select(*lists)    
    print("time: %.5f" % (time.time() - start_time))
    print(results)
