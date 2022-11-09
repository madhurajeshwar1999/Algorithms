import random
import sys

def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        # i = random.randint(0, len(a) - 1)
        # pivot = a[i]
        # a[0], a[i] = a[i], a[0]  # put the pivot element in 0-index

        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def insertion(a, v):
    left = a[0]
    root = a[1]
    right = a[2]

    if v < root:
        if not left:
            left.extend([[], v, []])
        else:
            insertion(left, v)
    elif v == root: # already in tree, do nothing
        pass
    else:
        if not right:
            right.extend([[], v, []])
        else:
            insertion(right, v)

maxlen = 10
maxvalue = 20

print("from qsort import sort, sorted, search, insert")

for _ in range(10):
    # genreate a list of integers
    length = random.randint(1, maxlen)
    arr = random.sample(range(1, maxvalue), length)
    print("arr =", arr)

    # generate tree
    tree = sort(arr)
    print("tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)")
    print("assert tree == %s, tree" % tree)

    # sorted in-order traverse
    print("assert sorted(tree) == %s, tree" % sorted(arr))

    # search
    for __ in range(10):
        if_in_arr = random.randint(0, 1)
        if if_in_arr:
            selected = arr[random.randint(1, length)-1]
            print("assert search(tree, %d) == True, tree" % selected)
        else:
            selected = random.randint(1, maxvalue)
            while selected in arr:
                selected = random.randint(1, maxvalue)
            # must be out of arr
            print("assert search(tree, %d) == False, tree" % selected)

    for __ in range(10):
        # insertion
        selected = random.randint(1, maxvalue)
        print("insert(tree, %d)" % selected)
        insertion(tree, selected)
        print("assert tree == %s, tree" % tree)
        print()

print("print('all passed!')")
