import random

# intro2cs summary for the exam:

# False values - False, 0, 0.0, None, "", []

# **Running times**
# every loop till range(n) is O(n), for example if there are 2 nested loops
# till n the running time will be O(n^2), if there are 2 regular loops it's
# supposed to be 2n, but it really stays O(n) no matter how many loops there
# are as long as their not nested. for binary search or for an algorithm with
# one loop on a list in len n that we cut into half every round of it, it's
# O(log(n)). if there's one loop that runs till range(2**n) the running time
# will be O(2^n).
# running times from best to worse:
# O(log(n)), O(n), O(n*log(n)), O(n^2), O(2^n), O(n!).

# **constructors for list**
# list(), [list, stuff], lst1 + lst2 = [lst1, lst2],
# [obj]*n = [obj, obj, ...., obj] - n times.

# list comprehension vs. generator expressions: listcomp = [x**2 for x in seq],
# genexp = (x**2 for x in seq). main differences:
# Genexp could be used only once, you cannot access a genexp using [], or any
# other list method. a genexp requires less memory.

# **common edge cases**
# division or modulo by zero, list index out of range,
# "next" of a node is None, "odd inputs"- such as negative numbers or strings
# when expecting positive integer (for example for grades), etc..

# **slicing**
# works for lists, strings and tuples. for example: list[:2] is the 2
# first indexes of the list, list[2:] is the list from the third index,
# list[:] makes a shallow copy of the list, changing this copy won't change the
# original, list[::2] is the even indexes of the list (the list in jumps of 2),
# list[::-1] is the list backwards, list[:-1] is the regular list without the
# last index, list[1:5:2] is the list from the second index to the 4th index in
# jumps of 2 indexes each time. for example: list = [1, 2, 3, 4, 5],
# list[1:5:2] = [2, 4]. there's also an option of assignment of lists and
# deleting from lists (works only on lists!) by slicing, for example:
# on the same list, list[2:4] = [7, 8, 9], list will be now: [1, 2, 7, 8, 9, 5]
# del list[::2], list will be now: [2, 8, 5]

# **enumerate**
# when printing i in enumerate(list), the printed value will be a
# tuple of (index, index value), for example: seasons = ['Spring', 'Summer ',
# 'Fall', 'Winter'], for i in enumerate(seasons): print(i)
# print value: (0, 'Spring'), (1, 'Summer '), (2, 'Fall'), (3, 'Winter')
# note: works on numbers too

# **sets**
# each value appears only ones in a set. for example set([1,2,1,2]) = {1,2}

# **recursion**
# divide and conquer: in order to solve a problem, solve a similar problem of
# smaller size. think only about how to use the smaller solution to get the
# larger one, and what is the base case.

# **linked lists**
# class Node: contains data and "next", a pointer which leads to the next Node
# linked to the current Node. the next of the last Node is "None". the "head"
# of the linked list is the first Node. important edge case- reaching None at
# the end of the list.
# Doubly-linked lists: has 2 ways pointers- both prev and next.
# examples:
# printing a linked list:
def print_linked_list(head):
    cur = head
    while cur != None:
        print(cur.data)
        cur = cur.next
# inserting a new node to the linked list:
def add_node(cur):
    cur.next = Node("some value", cur.next)
# removing a node from the linked list:
def remove_node(cur):
    cur.next = cur.next.next

# tree nodes: the head node is the root, the nodes that are linked directly to
# it (underneath it) are called it's child's and it is called their parent. in
# class Treenode we'll use left and right instead of prev and next. when
# searching an item on a treenode, worst case would be O(n) runtime.

# **iterators**
# iterators are objects that repeatedly return new values. they have a built-in
# function next() which calls the next value of the iterator.
# the function iter() creates an iterator out of iterable objects.

# **generators**
# the easiest way to create an iterator. we use the method "yield", and then
# the "next" of the iterator will be the thing we yield each time. we can
# combine Treenodes with generators and create an iterator for the tree's
# values. for example:
class Treenode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __iter__(self):
        yield self.data
        if self.left:
            for item in self.left:
                yield item
        if self.right:
            for item in self.right:
                yield item

# **map, filter and reduce**

# map - gets a function and a sequence and activates the function on each
# element of sequence, and creates an iterable object of the results.
# filter - gets a function and a sequence, It applies function to each element
# of the sequence. If function returns True for that element then the element
# is put into a List.
# reduce - gets a function and applies it on each element of the sequence, with
# the sum before it, meaning it works on the 2 first elements, then on the
# third with the summation of the 2 first, etc.. reduce needs import to
# functools before calling it, and then the use is: functools.recuce(f, seq).
# examples:
# list(map(lambda x: x*x, range(7))) = [0, 1, 4, 9, 16, 25, 36]
# list(filter(lambda x: x%2 != 0, [7, 5, 4, 3, 2, 6, 1])) = [7, 5, 3, 1]
# import functools
# functools.reduce(lambda x, y: x*y, range(1, 6)) = 120

# **important algorithms**

# **Binary search** (running time: O(log(n)))
# general idea = we start the search from the min val to the mid val(becomes
# max val). if the value is between them we continue to search between the min
# val and the new mid val (between the min and new max = old mid), else the max
# val becomes the min val and the new max val becomes the original max val,
# then we continue searching by converting the min\max val to the new mid val
# each time in compatible to the value we're searching until we find it.

# example to binary search:
def binary_search(val,L):
    lo, hi = 0, len(L)
    while lo < hi:
        mid = (lo+hi)//2
        mid_val = L[mid]
        if val > mid_val:
            lo = mid+1
        elif val < L[mid]:
            hi = mid
        else:
            return mid
    return None

# Types of sorts:
# Bubble sort: (running time: O(n^2))
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

# Quick sort: (running time: on average it's O(n*log(n)), worst case is O(n^2)
# but this behavior is rare)

def quicksort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
    less = quicksort(less)
    more = quicksort(more)
    return less + pivotList + more

# Radix Sort: (running time: k*(n+b) steps, meaning O(n) for b, k small enough)
def radixsort(lst, radix=10):
    max_val = max(lst)
    power = 0
    while radix**power < max_val:
        power += 1
    for p in range(power):
        factor = radix**p
        buckets = [list() for d in range(radix)]
        for val in lst:
            tmp = val/factor
            buckets[int(tmp % radix)].append(val)
        lst = []
        for b in range(radix):
            buck = buckets[b]
            for val in buck:
                lst.append(val)
    return lst

# Merge sort: (running time: O(n*log(n)):
def merge(b, c, list):
    i, j, k = 0, 0, 0
    while k < len(list):
        if i < len(b) and (j >= len(c) or b[i] < c[j]):
            list[k] = b[i]
            i += 1
        else:
            list[k] = c[j]
            j += 1
        k += 1
    return list

def merge_sort(list):
    if len(list) == 1:
        return
    else:
        mid = len(list)//2
        b = list[:mid]
        c = list[mid:]
        merge_sort(b)
        merge_sort(c)
        merge(b, c, list)
    return list