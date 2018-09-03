#we are given this class:
class Node(object): 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next

# part a: for a linked list of length n, The time complexity is O(n^2). 
# In the worst case there is no cycle. The while loop runs n times, each time 
# the list past grows by one, and we check if "cur in past" which is linear in the length of past.
# in total, we do 1+2+...+(n-1).
#
# The space complexity is O(n) due to the need to store the list "past"

#part b:
def node_i(head,i):
    if i<0:
        return None
    while head and i>0:
        i=i-1
        head = head.next
    return head

#part c: (assumes list is circular, non-empty, and returns to head)
def cycle_length(head):
    result = 1
    cur = head.next
    while cur is not head:
        cur = cur.next
        result+=1
    return result

#part d: assumes there is an index i in the list such that 
#the i'th item and the (2i+1)'th item are the same
def find_loop(head):
    i=0
    first = head
    second = head.next
    while first is not second:
        i+=1
        first= first.next
        second = second.next.next
    return i

#part e: This part relies strongly on the solution to the previous part. 
# if the condition of part d does occur, then we have a loop, otherwise we do not.
# we just need to change return values to True/False instead of the index i, and we
# must be careful not to "fall off the edge" of the list if there is no loop.
def has_cycle(head):
    if not head or not head.next:
        return False
    first = head
    second = head.next
    while first is not second:
        first= first.next
        if not second.next or not second.next.next:
            return False
        second = second.next.next
    return True
