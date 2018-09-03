#!/usr/bin/env python3

def subsets(lst):
    if len(lst)==0:
        yield []
    else:
        for tail in subsets(lst[1:]):
            yield tail
            yield [lst[0]]+tail

#A:
print(list(subsets([1,5,3])))
#[[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]

#B:
def filtered_subsets(lst, max_sum):
    return filter(lambda s: sum(s) <= max_sum, subsets(lst))

#print(list(filtered_subsets([1,5,3],4)))
#[[], [1], [3], [1, 3]]

#C:
def bounded_subsets(lst, max_sum):
    if len(lst)==0:
        if max_sum>=0:
            yield []
    else:
        for tail in bounded_subsets(lst[1:], max_sum):
            yield tail
            if sum(tail)+lst[0] <= max_sum:
                yield [lst[0]]+tail

#print(list(bounded_subsets([1,5,3],4)))
#[[], [1], [3], [1, 3]]

#D:
#print(list(filtered_subsets([-1,1],0)))
#[[], [-1], [-1, 1]]
#print(list(bounded_subsets([-1,1],0)))
#[[], [-1]]

#E:
def doubly_bounded_subsets(lst, min_sum, max_sum):
    if len(lst)==0:
        if min_sum<=0 and max_sum>=0:
            yield []
    else:
        for tail in doubly_bounded_subsets(lst[1:], min_sum-lst[0], max_sum):
            if  min_sum <= sum(tail) <= max_sum:
                yield tail
            if  min_sum <= sum(tail)+lst[0] <= max_sum:
                yield [lst[0]]+tail

#print(list(doubly_bounded_subsets([1,5,3],0,4)))
#[[], [1], [3], [1, 3]]
#print(list(doubly_bounded_subsets([1,5,3],2,4)))
#[[3], [1, 3]]

#Side question: Can you find the bug in subsets()?

def failed_subsets(lst):
    for i,ss in enumerate(subsets(lst)):
        ss.append(i)
        yield ss

#print(list(failed_subsets([1,5,3])))
