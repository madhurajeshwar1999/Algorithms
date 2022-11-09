#!/usr/bin/env python3

import random
import time
import heapq

def gen(n):
    random.seed(1)
    return random.sample(list(range(n)), n)

for n in [5000, 10000, 20000, 40000, 80000, 160000]:
    a = gen(n)
    h = a.copy()
    t = time.time()
    heapq.heapify(h)
    t1 = time.time()
    h = []
    for x in a:
        heapq.heappush(h, x)
    t2 = time.time()
    print(n, t1-t, t2-t1)
    
