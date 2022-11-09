from qsort import sort, sorted, search, insert
arr = [15, 19, 3, 1, 16, 14, 8, 7, 17, 13]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree
assert sorted(tree) == [1, 3, 7, 8, 13, 14, 15, 16, 17, 19], tree
assert search(tree, 1) == True, tree
assert search(tree, 9) == False, tree
assert search(tree, 2) == False, tree
assert search(tree, 8) == True, tree
assert search(tree, 18) == False, tree
assert search(tree, 19) == True, tree
assert search(tree, 17) == True, tree
assert search(tree, 19) == True, tree
assert search(tree, 4) == False, tree
assert search(tree, 19) == True, tree
insert(tree, 15)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 7)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 1)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 14)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 10)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[[], 10, []], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 14)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[[], 10, []], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 17)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[[], 10, []], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 3)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[[], 10, []], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 7)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[[], 10, []], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, []]], tree

insert(tree, 20)
assert tree == [[[[], 1, []], 3, [[[[], 7, []], 8, [[[], 10, []], 13, []]], 14, []]], 15, [[[], 16, [[], 17, []]], 19, [[], 20, []]]], tree

arr = [18, 17, 1, 11, 9]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[[[], 1, [[[], 9, []], 11, []]], 17, []], 18, []], tree
assert sorted(tree) == [1, 9, 11, 17, 18], tree
assert search(tree, 17) == True, tree
assert search(tree, 5) == False, tree
assert search(tree, 1) == True, tree
assert search(tree, 9) == True, tree
assert search(tree, 18) == True, tree
assert search(tree, 18) == True, tree
assert search(tree, 16) == False, tree
assert search(tree, 1) == True, tree
assert search(tree, 13) == False, tree
assert search(tree, 2) == False, tree
insert(tree, 20)
assert tree == [[[[], 1, [[[], 9, []], 11, []]], 17, []], 18, [[], 20, []]], tree

insert(tree, 9)
assert tree == [[[[], 1, [[[], 9, []], 11, []]], 17, []], 18, [[], 20, []]], tree

insert(tree, 5)
assert tree == [[[[], 1, [[[[], 5, []], 9, []], 11, []]], 17, []], 18, [[], 20, []]], tree

insert(tree, 3)
assert tree == [[[[], 1, [[[[[], 3, []], 5, []], 9, []], 11, []]], 17, []], 18, [[], 20, []]], tree

insert(tree, 15)
assert tree == [[[[], 1, [[[[[], 3, []], 5, []], 9, []], 11, [[], 15, []]]], 17, []], 18, [[], 20, []]], tree

insert(tree, 15)
assert tree == [[[[], 1, [[[[[], 3, []], 5, []], 9, []], 11, [[], 15, []]]], 17, []], 18, [[], 20, []]], tree

insert(tree, 6)
assert tree == [[[[], 1, [[[[[], 3, []], 5, [[], 6, []]], 9, []], 11, [[], 15, []]]], 17, []], 18, [[], 20, []]], tree

insert(tree, 15)
assert tree == [[[[], 1, [[[[[], 3, []], 5, [[], 6, []]], 9, []], 11, [[], 15, []]]], 17, []], 18, [[], 20, []]], tree

insert(tree, 16)
assert tree == [[[[], 1, [[[[[], 3, []], 5, [[], 6, []]], 9, []], 11, [[], 15, [[], 16, []]]]], 17, []], 18, [[], 20, []]], tree

insert(tree, 11)
assert tree == [[[[], 1, [[[[[], 3, []], 5, [[], 6, []]], 9, []], 11, [[], 15, [[], 16, []]]]], 17, []], 18, [[], 20, []]], tree

arr = [1, 3, 8, 6, 19, 10]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[], 1, [[], 3, [[[], 6, []], 8, [[[], 10, []], 19, []]]]], tree
assert sorted(tree) == [1, 3, 6, 8, 10, 19], tree
assert search(tree, 8) == True, tree
assert search(tree, 4) == False, tree
assert search(tree, 4) == False, tree
assert search(tree, 18) == False, tree
assert search(tree, 5) == False, tree
assert search(tree, 3) == True, tree
assert search(tree, 19) == True, tree
assert search(tree, 8) == True, tree
assert search(tree, 2) == False, tree
assert search(tree, 2) == False, tree
insert(tree, 13)
assert tree == [[], 1, [[], 3, [[[], 6, []], 8, [[[], 10, [[], 13, []]], 19, []]]]], tree

insert(tree, 16)
assert tree == [[], 1, [[], 3, [[[], 6, []], 8, [[[], 10, [[], 13, [[], 16, []]]], 19, []]]]], tree

insert(tree, 4)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[], 13, [[], 16, []]]], 19, []]]]], tree

insert(tree, 18)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[], 13, [[], 16, [[], 18, []]]]], 19, []]]]], tree

insert(tree, 20)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[], 13, [[], 16, [[], 18, []]]]], 19, [[], 20, []]]]]], tree

insert(tree, 20)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[], 13, [[], 16, [[], 18, []]]]], 19, [[], 20, []]]]]], tree

insert(tree, 8)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[], 13, [[], 16, [[], 18, []]]]], 19, [[], 20, []]]]]], tree

insert(tree, 1)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[], 13, [[], 16, [[], 18, []]]]], 19, [[], 20, []]]]]], tree

insert(tree, 11)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[[], 11, []], 13, [[], 16, [[], 18, []]]]], 19, [[], 20, []]]]]], tree

insert(tree, 1)
assert tree == [[], 1, [[], 3, [[[[], 4, []], 6, []], 8, [[[], 10, [[[], 11, []], 13, [[], 16, [[], 18, []]]]], 19, [[], 20, []]]]]], tree

arr = [11, 16, 13, 2, 14, 9, 4, 18, 6, 3]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[[], 2, [[[[], 3, []], 4, [[], 6, []]], 9, []]], 11, [[[], 13, [[], 14, []]], 16, [[], 18, []]]], tree
assert sorted(tree) == [2, 3, 4, 6, 9, 11, 13, 14, 16, 18], tree
assert search(tree, 1) == False, tree
assert search(tree, 20) == False, tree
assert search(tree, 1) == False, tree
assert search(tree, 17) == False, tree
assert search(tree, 9) == True, tree
assert search(tree, 5) == False, tree
assert search(tree, 20) == False, tree
assert search(tree, 14) == True, tree
assert search(tree, 11) == True, tree
assert search(tree, 17) == False, tree
insert(tree, 5)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, []]], 9, []]], 11, [[[], 13, [[], 14, []]], 16, [[], 18, []]]], tree

insert(tree, 12)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, []]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, []]]], tree

insert(tree, 6)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, []]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, []]]], tree

insert(tree, 3)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, []]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, []]]], tree

insert(tree, 13)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, []]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, []]]], tree

insert(tree, 7)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, [[], 7, []]]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, []]]], tree

insert(tree, 20)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, [[], 7, []]]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, [[], 20, []]]]], tree

insert(tree, 5)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, [[], 7, []]]], 9, []]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, [[], 20, []]]]], tree

insert(tree, 10)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, [[], 7, []]]], 9, [[], 10, []]]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, [[], 20, []]]]], tree

insert(tree, 16)
assert tree == [[[], 2, [[[[], 3, []], 4, [[[], 5, []], 6, [[], 7, []]]], 9, [[], 10, []]]], 11, [[[[], 12, []], 13, [[], 14, []]], 16, [[], 18, [[], 20, []]]]], tree

arr = [12, 6, 1, 9, 10]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[[[], 1, []], 6, [[], 9, [[], 10, []]]], 12, []], tree
assert sorted(tree) == [1, 6, 9, 10, 12], tree
assert search(tree, 9) == True, tree
assert search(tree, 11) == False, tree
assert search(tree, 12) == True, tree
assert search(tree, 14) == False, tree
assert search(tree, 20) == False, tree
assert search(tree, 12) == True, tree
assert search(tree, 9) == True, tree
assert search(tree, 2) == False, tree
assert search(tree, 14) == False, tree
assert search(tree, 12) == True, tree
insert(tree, 9)
assert tree == [[[[], 1, []], 6, [[], 9, [[], 10, []]]], 12, []], tree

insert(tree, 3)
assert tree == [[[[], 1, [[], 3, []]], 6, [[], 9, [[], 10, []]]], 12, []], tree

insert(tree, 12)
assert tree == [[[[], 1, [[], 3, []]], 6, [[], 9, [[], 10, []]]], 12, []], tree

insert(tree, 1)
assert tree == [[[[], 1, [[], 3, []]], 6, [[], 9, [[], 10, []]]], 12, []], tree

insert(tree, 8)
assert tree == [[[[], 1, [[], 3, []]], 6, [[[], 8, []], 9, [[], 10, []]]], 12, []], tree

insert(tree, 6)
assert tree == [[[[], 1, [[], 3, []]], 6, [[[], 8, []], 9, [[], 10, []]]], 12, []], tree

insert(tree, 9)
assert tree == [[[[], 1, [[], 3, []]], 6, [[[], 8, []], 9, [[], 10, []]]], 12, []], tree

insert(tree, 14)
assert tree == [[[[], 1, [[], 3, []]], 6, [[[], 8, []], 9, [[], 10, []]]], 12, [[], 14, []]], tree

insert(tree, 16)
assert tree == [[[[], 1, [[], 3, []]], 6, [[[], 8, []], 9, [[], 10, []]]], 12, [[], 14, [[], 16, []]]], tree

insert(tree, 12)
assert tree == [[[[], 1, [[], 3, []]], 6, [[[], 8, []], 9, [[], 10, []]]], 12, [[], 14, [[], 16, []]]], tree

arr = [12, 17, 13, 6, 4, 19, 14, 15]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[[[], 4, []], 6, []], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, []]]], tree
assert sorted(tree) == [4, 6, 12, 13, 14, 15, 17, 19], tree
assert search(tree, 4) == True, tree
assert search(tree, 3) == False, tree
assert search(tree, 10) == False, tree
assert search(tree, 13) == True, tree
assert search(tree, 13) == True, tree
assert search(tree, 12) == True, tree
assert search(tree, 3) == False, tree
assert search(tree, 13) == True, tree
assert search(tree, 2) == False, tree
assert search(tree, 20) == False, tree
insert(tree, 12)
assert tree == [[[[], 4, []], 6, []], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, []]]], tree

insert(tree, 19)
assert tree == [[[[], 4, []], 6, []], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, []]]], tree

insert(tree, 4)
assert tree == [[[[], 4, []], 6, []], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, []]]], tree

insert(tree, 9)
assert tree == [[[[], 4, []], 6, [[], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, []]]], tree

insert(tree, 20)
assert tree == [[[[], 4, []], 6, [[], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, [[], 20, []]]]], tree

insert(tree, 5)
assert tree == [[[[], 4, [[], 5, []]], 6, [[], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, [[], 20, []]]]], tree

insert(tree, 20)
assert tree == [[[[], 4, [[], 5, []]], 6, [[], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[], 19, [[], 20, []]]]], tree

insert(tree, 18)
assert tree == [[[[], 4, [[], 5, []]], 6, [[], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[[], 18, []], 19, [[], 20, []]]]], tree

insert(tree, 14)
assert tree == [[[[], 4, [[], 5, []]], 6, [[], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[[], 18, []], 19, [[], 20, []]]]], tree

insert(tree, 8)
assert tree == [[[[], 4, [[], 5, []]], 6, [[[], 8, []], 9, []]], 12, [[[], 13, [[], 14, [[], 15, []]]], 17, [[[], 18, []], 19, [[], 20, []]]]], tree

arr = [2, 18, 7, 15, 19, 13, 6, 9]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[], 9, []], 13, []], 15, []]], 18, [[], 19, []]]], tree
assert sorted(tree) == [2, 6, 7, 9, 13, 15, 18, 19], tree
assert search(tree, 20) == False, tree
assert search(tree, 6) == True, tree
assert search(tree, 2) == True, tree
assert search(tree, 6) == True, tree
assert search(tree, 3) == False, tree
assert search(tree, 2) == True, tree
assert search(tree, 4) == False, tree
assert search(tree, 6) == True, tree
assert search(tree, 17) == False, tree
assert search(tree, 20) == False, tree
insert(tree, 7)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[], 9, []], 13, []], 15, []]], 18, [[], 19, []]]], tree

insert(tree, 13)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[], 9, []], 13, []], 15, []]], 18, [[], 19, []]]], tree

insert(tree, 20)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[], 9, []], 13, []], 15, []]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 19)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[], 9, []], 13, []], 15, []]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 8)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[[], 8, []], 9, []], 13, []], 15, []]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 14)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[[], 8, []], 9, []], 13, [[], 14, []]], 15, []]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 7)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[[], 8, []], 9, []], 13, [[], 14, []]], 15, []]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 6)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[[], 8, []], 9, []], 13, [[], 14, []]], 15, []]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 16)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[[], 8, []], 9, []], 13, [[], 14, []]], 15, [[], 16, []]]], 18, [[], 19, [[], 20, []]]]], tree

insert(tree, 15)
assert tree == [[], 2, [[[[], 6, []], 7, [[[[[], 8, []], 9, []], 13, [[], 14, []]], 15, [[], 16, []]]], 18, [[], 19, [[], 20, []]]]], tree

arr = [14]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[], 14, []], tree
assert sorted(tree) == [14], tree
assert search(tree, 18) == False, tree
assert search(tree, 14) == True, tree
assert search(tree, 12) == False, tree
assert search(tree, 14) == True, tree
assert search(tree, 14) == True, tree
assert search(tree, 10) == False, tree
assert search(tree, 6) == False, tree
assert search(tree, 14) == True, tree
assert search(tree, 5) == False, tree
assert search(tree, 14) == True, tree
insert(tree, 8)
assert tree == [[[], 8, []], 14, []], tree

insert(tree, 6)
assert tree == [[[[], 6, []], 8, []], 14, []], tree

insert(tree, 13)
assert tree == [[[[], 6, []], 8, [[], 13, []]], 14, []], tree

insert(tree, 9)
assert tree == [[[[], 6, []], 8, [[[], 9, []], 13, []]], 14, []], tree

insert(tree, 6)
assert tree == [[[[], 6, []], 8, [[[], 9, []], 13, []]], 14, []], tree

insert(tree, 4)
assert tree == [[[[[], 4, []], 6, []], 8, [[[], 9, []], 13, []]], 14, []], tree

insert(tree, 10)
assert tree == [[[[[], 4, []], 6, []], 8, [[[], 9, [[], 10, []]], 13, []]], 14, []], tree

insert(tree, 20)
assert tree == [[[[[], 4, []], 6, []], 8, [[[], 9, [[], 10, []]], 13, []]], 14, [[], 20, []]], tree

insert(tree, 7)
assert tree == [[[[[], 4, []], 6, [[], 7, []]], 8, [[[], 9, [[], 10, []]], 13, []]], 14, [[], 20, []]], tree

insert(tree, 14)
assert tree == [[[[[], 4, []], 6, [[], 7, []]], 8, [[[], 9, [[], 10, []]], 13, []]], 14, [[], 20, []]], tree

arr = [17, 18]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[], 17, [[], 18, []]], tree
assert sorted(tree) == [17, 18], tree
assert search(tree, 17) == True, tree
assert search(tree, 18) == True, tree
assert search(tree, 17) == True, tree
assert search(tree, 19) == False, tree
assert search(tree, 18) == True, tree
assert search(tree, 2) == False, tree
assert search(tree, 6) == False, tree
assert search(tree, 18) == True, tree
assert search(tree, 20) == False, tree
assert search(tree, 18) == True, tree
insert(tree, 5)
assert tree == [[[], 5, []], 17, [[], 18, []]], tree

insert(tree, 16)
assert tree == [[[], 5, [[], 16, []]], 17, [[], 18, []]], tree

insert(tree, 14)
assert tree == [[[], 5, [[[], 14, []], 16, []]], 17, [[], 18, []]], tree

insert(tree, 3)
assert tree == [[[[], 3, []], 5, [[[], 14, []], 16, []]], 17, [[], 18, []]], tree

insert(tree, 4)
assert tree == [[[[], 3, [[], 4, []]], 5, [[[], 14, []], 16, []]], 17, [[], 18, []]], tree

insert(tree, 2)
assert tree == [[[[[], 2, []], 3, [[], 4, []]], 5, [[[], 14, []], 16, []]], 17, [[], 18, []]], tree

insert(tree, 19)
assert tree == [[[[[], 2, []], 3, [[], 4, []]], 5, [[[], 14, []], 16, []]], 17, [[], 18, [[], 19, []]]], tree

insert(tree, 13)
assert tree == [[[[[], 2, []], 3, [[], 4, []]], 5, [[[[], 13, []], 14, []], 16, []]], 17, [[], 18, [[], 19, []]]], tree

insert(tree, 9)
assert tree == [[[[[], 2, []], 3, [[], 4, []]], 5, [[[[[], 9, []], 13, []], 14, []], 16, []]], 17, [[], 18, [[], 19, []]]], tree

insert(tree, 11)
assert tree == [[[[[], 2, []], 3, [[], 4, []]], 5, [[[[[], 9, [[], 11, []]], 13, []], 14, []], 16, []]], 17, [[], 18, [[], 19, []]]], tree

arr = [5, 10, 11, 2, 16, 8, 14]
tree = sort(arr) # choose the first element as pivot (randomized pivot results in different trees)
assert tree == [[[], 2, []], 5, [[[], 8, []], 10, [[], 11, [[[], 14, []], 16, []]]]], tree
assert sorted(tree) == [2, 5, 8, 10, 11, 14, 16], tree
assert search(tree, 17) == False, tree
assert search(tree, 18) == False, tree
assert search(tree, 4) == False, tree
assert search(tree, 11) == True, tree
assert search(tree, 16) == True, tree
assert search(tree, 11) == True, tree
assert search(tree, 1) == False, tree
assert search(tree, 10) == True, tree
assert search(tree, 11) == True, tree
assert search(tree, 9) == False, tree
insert(tree, 15)
assert tree == [[[], 2, []], 5, [[[], 8, []], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 10)
assert tree == [[[], 2, []], 5, [[[], 8, []], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 4)
assert tree == [[[], 2, [[], 4, []]], 5, [[[], 8, []], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 7)
assert tree == [[[], 2, [[], 4, []]], 5, [[[[], 7, []], 8, []], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 3)
assert tree == [[[], 2, [[[], 3, []], 4, []]], 5, [[[[], 7, []], 8, []], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 9)
assert tree == [[[], 2, [[[], 3, []], 4, []]], 5, [[[[], 7, []], 8, [[], 9, []]], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 1)
assert tree == [[[[], 1, []], 2, [[[], 3, []], 4, []]], 5, [[[[], 7, []], 8, [[], 9, []]], 10, [[], 11, [[[], 14, [[], 15, []]], 16, []]]]], tree

insert(tree, 19)
assert tree == [[[[], 1, []], 2, [[[], 3, []], 4, []]], 5, [[[[], 7, []], 8, [[], 9, []]], 10, [[], 11, [[[], 14, [[], 15, []]], 16, [[], 19, []]]]]], tree

insert(tree, 16)
assert tree == [[[[], 1, []], 2, [[[], 3, []], 4, []]], 5, [[[[], 7, []], 8, [[], 9, []]], 10, [[], 11, [[[], 14, [[], 15, []]], 16, [[], 19, []]]]]], tree

insert(tree, 15)
assert tree == [[[[], 1, []], 2, [[[], 3, []], 4, []]], 5, [[[[], 7, []], 8, [[], 9, []]], 10, [[], 11, [[[], 14, [[], 15, []]], 16, [[], 19, []]]]]], tree

print('all passed!')
