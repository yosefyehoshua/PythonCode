#!/usr/bin/env python3

#######
#
# Q1 solution
#
#######


a = [0,1,2,3,4,5,6,7,8,9]
#1.1
print(a[8:2:2])   #answer: []                                                 
print(a[ :2:-2])  #[9, 7, 5, 3]
print(a[8: :-2])  #[8, 6, 4, 2, 0] 

def rev(s):
   return s[ : :-1]
#1.2
print(rev('beauty'))  #ytuaeb

def f(s):
   if len(s) < 2:
       return s
   else:
       s2 = s[0:2]

       if s[0] > s[1]:
           s2 = rev(s2)
       return s2[0] + f(s2[1]+s[2:])

#1.3
print(f('beauty')) #baetuy


#1.4: A correction such that f will work with ints:

#  return s2[0] + f(s2[1]+s[2:]) ->  return [s2[0]] + f([s2[1]]+s[2:])


def foo(s, n):
   s1 = s
   for i in range(n):
       s1 = f(s1)
   return s1
#1.5
print(foo('beauty', 2)) # abetuy  
print(foo('beauty', len('beauty')))   # abetuy

def fooy(s, i, b):
   if i >= len(s)//2:
       return ''  # empty string
   else:
       s2 = s[i] + s[i+len(s)//2]
       if b:
           s2 = rev(s2)
       return s2 + fooy(s, i+1, b)

#1.6
print(fooy('beauty', 0, False)) #buetay                            
print(fooy('beauty', 0, True))  #ubteya

#1.7: what will happen if in fooy we'll replace last command to: 
#return s2 + fooy(s, i+1, not b)

def fooy_7(s, i, b):
   if i >= len(s)//2:
       return ''  # empty string
   else:
       s2 = s[i] + s[i+len(s)//2]
       if b:
           s2 = rev(s2)
       return s2 + fooy(s, i+1, b)


print(fooy_7('beauty', 0, False)) #buteay
#1.9
print(foo(fooy('beauty', 0, False), 5)) #abetuy                   

#1.10
print(fooy(foo('beauty', 5), 0, True)) #taubye                      














#######
#
# Q2 solution:
#
#######

class Node:
     def __init__(self, data, next_node=None):
          self.data = data
          self.next = next_node

#2.1
def len_list(head):
    length = 0
    while head is not None:
        length+=1
        head=head.next

    return length

#2.2
def node_i(head,idx):
    if idx<0: # If the index is negative then idx = len+idx
        L=len_list(head)
        idx = L+idx
        if idx<0:
            return None

    while idx>0 and head is not None:
        head=head.next
        idx-=1
    return head

#2.3
def is_tail(head_x,head_y):
    if not head_x or not head_y:
        return False

    # Run until we reached the end of x or found a shared Node
    # We note that it's enough that we found one joint node to declare tail
    while head_x is not None and head_x != head_y: 
        head_x=head_x.next

    if not head_x: # We reached the end of x
        return False
    
    return True 
    
   
#2.4
def are_joint(head_x,head_y):
    if not head_x or not head_y:
        return None
    len_x = len_list(head_x)
    len_y = len_list(head_y)
    cur_x = node_i(head_x,max(0,len_x-len_y))
    cur_y = node_i(head_y,max(0,len_y-len_x))

    # Now len_list(cur_x)==len_list(cur_y)
    
    # Run until we reached the end of the lists
    # or we found a joint Node.
    # Again it's enough to find one shared Node to declare joint lists  
    while cur_x and cur_x !=cur_y:
        cur_x=cur_x.next
        cur_y=cur_y.next

    if not cur_x: 
        return None
    return cur_x

#2.5
def copy_list_until(other,last=None):
    """copy the linked list that starts with other,
    stop copying when reaching last.
    return a pointer to the new head and to tail of the new list"""
    if other is last: 
        return(None,None)
    head_new =  Node(other.data)
    cur_new = head_new
    other = other.next
    while other is not last: #joint node or None - the end of the list
        cur_new.next = Node(other.data)
        cur_new= cur_new.next
        other = other.next

    return(head_new,cur_new)    
    
def combine(head_x,head_y):
    possible_joint_node = are_joint(head_x,head_y)
    new_head,temp_tail = copy_list_until(head_x) # copy the entire x list
    temp_head,tail = copy_list_until(head_y,possible_joint_node) # copy y only until the shared Node
    
    temp_tail.next = temp_head

    return new_head




#######
#
# Q3 solution:
#
#######

import math

BASE = 10
#3.1
def digit_generator1(num):
    ''' A simple digit generator which generates the digits in order '''
    if num == 0:
        return
        # Dealing with 0 was not required, but it can't hurt.
        # There are two reasonable results for an input of 0:
        # a single digit number '0', or an empty number ''.

    factor = BASE ** int(math.log(num,BASE))
    # Or any other method of counting the number of digits.
    # Be careful, since counting the digits with something equivalent
    # to Watch out, though,  for that the equivalent of
    #factor = BASE ** len(str(num))
    # will add a leading 0 to the number.
    # Uncommenting the previous line will demonstrate that.

    # A correct method using a loop to count the length could be:
    #factor = 1
    #while factor * BASE <= num:
    #    factor *= BASE

    while factor > 0:
        # Do not use num in the loop condition. That would cause the 
        # generator for a number divisible by BASE to fail.
        yield num // factor
        num %= factor
        factor //= BASE
        # You can't recalculate the factor during each iteration, as that
        # causes you to miss 0s in trhe middle of the number.

def digit_generator2(num):
    ''' A simple digit generator which generates the digits in reverse.
    The calculations are simpler, but you need to store a stack. '''
    digits = []
    while num > 0:
        digits.append(num % BASE)
        num //= BASE
    while digits:
        # return digits[::-1] would be iterable, but would not be an iterator.
        yield digits.pop()
        # or any other returning of the digits in reverse.

def digit_generator3(num):
    ''' A more "elegant" solution, though I don't actually recomment using it.
    When wouldn't it work? '''
    if num <= 0:
        return
    for digit in digit_generator3(num // BASE):
        yield digit
    yield num % BASE

def digit_generator4(num):
    ''' A one liner. Do not even think about doing something like this 
    in a test, and usually not at all. '''
    return (num // BASE ** i % BASE for i in range(int(math.log(max(num,1),BASE)),-1,-1))

class digit_iterator1(object):
    ''' A simple digit iterator. There is no advantage to this over
    the generator in this case'''

    def __init__(self, num):
        self.num = num
        if num == 0:
            self.factor = 0
            # We can't just return here
        else:
            self.factor = BASE ** int(math.log(num,BASE))
            # The factor has to be saved for the same reason it needs to be
            # saved in the generator.

    def __iter__(self):
        return self
        # Otherwise it isn't an iterator...

    def __next__(self):
        if self.factor == 0:
            raise StopIteration
            # Must be explicit

        # No loop, as we are returning the values
        digit = self.num // self.factor
        # or use divmod()
        # We need to return after updating the variables.
        self.num %= self.factor
        self.factor //= BASE
        return digit
        # Without the updating the variables, you will get a wrong answer.
        # Possibly also an infinite loop.

# There is no reason to nest a generator within a generator/iterator,
# or to have a separate function which just calls one and returns it.    

# Don't name your iterators 'iter' or '__iter__'. That is asking for trouble.
# int, len, str are also not good names.


#3.2:

digit_gen = digit_generator1
# Just to make it easy to switch generators below.


WIDTH = BASE - 1
# The fixed width was set to 9, because it is one less than the base used,
# and that limit is required by the variable width version. It is also
# to keep the constant independent, as you may choose a different width,
# narrower or wider, depending on the scenario.

class FixedWidthIntList(object):
    def __init__(self, list_of_ints):
        self.digit_list = []
        # You may not copy or store the list of ints, or use
        # any other variable length structure.
        for num in list_of_ints:
            digit_list = list(digit_gen(num))
            # You can calculate the length of the number before running
            # the generator, and then not need to save the list.
            # If you do that, it should be in a separate function.
            # Remember that len(num) will not work, as a number
            # is not iterable and does not have a length.

            self.digit_list += [0] * (WIDTH - len(digit_list)) + digit_list
            # Or:
            #self.digit_list += [[0] * WIDTH + digit_list][-WIDTH:]
            # Or use extend
            # Or append, adding each element in turn.
            # Do not use:
            #self.digit_list = self.digit_list + ...
            # As that changes the list creation to O(N^2)

    def __len__(self):
        return len(self.digit_list)//WIDTH

    def __iter__(self):
        # This object is not an iterator, so no return self.
        for i in range(len(self)):
            # It probably wouldn't hurt to also make a __len__ function
            yield self[i]
            # or self.__getitem__(i)
            # If you don't do this, you are probably duplicating code
            # with __getitem__

    def __getitem__(self, idx):
        if idx < 0 or idx >= len(self):
            # You can also allow negative indexes like in list
            return -1
    
        return digits_to_int(self.digit_list[idx*WIDTH:(idx+1)*WIDTH])
        # Will need to be repeated at least another time...


#3.3:

class VariableWidthIntList(object):
    def __init__(self, list_of_ints):
        self.digit_list = []

        for num in list_of_ints:
            digit_list = list(digit_gen(num))
            self.digit_list += [len(digit_list)] + digit_list
            # Note that within this class, 0 can be represented as '10' or '0'.
            # For that matter, leading 0s can be added to any number
            # up to the limit of 9 digits.

    # __len__ would be O(N)...

    def start_iter(self):
        ''' Iterator which returns the lengths and starting locations of
        ints in the digit list.
        Allows a slightly more efficient __getitem__ '''
        idx = 0
        while idx < len(self.digit_list):
            yield self.digit_list[idx], idx + 1
            idx += self.digit_list[idx] + 1
            # Remember the length of a number is its number of digits
            # plus a place for the length itself.

    def __iter__(self):
        for length, start in self.start_iter():
            yield digits_to_int(self.digit_list[start:start+length])

    def __getitem__(self, idx):
        if idx < 0:
            # We don't know what the length is.
            return -1

        # Without using the iterator, you are probably duplicating code.
        # The linear time cost for __getitem__ is the price we pay for
        # the smaller (usually) list size.

        for i,(length, start) in enumerate(self.start_iter()):
            # Or just enumerate the number list.
            # Of course do not store the list as you iterate over it.
            if i == idx:
                return digits_to_int(self.digit_list[start:start+length])
        return -1

def digits_to_int(digits):
    # This function can be modified to receive the full digit list, and
    # the relevant indexes.
    num = 0
    for digit in digits:
        num = num * BASE + digit
        # This is much simpler than keeping track of the multiplier factor.
        # Make sure when doing this that you take into account 0s in
        # middle of the number.
        # You can also access leading zeros without any special conditions.
    return num



#######
#
# Q4 solution:
#
#######



#part 1 

def intersect(segment1,segment2):
    return segment1[1]>= segment2[0] and segment2[1]>= segment1[0]


#part 2
def has_intersection(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if intersect(lst[i],lst[j]):
                return True
    return False

#part 3
def more_efficient_has_intersection(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if intersect(lst[i],lst[i+1]):
            return True
    return False
  
 
#part 4
# has_intersection runs in O(n^2) as it goes over all (n choose 2) pairs.
#  the more efficient version checks intersection in O(n) time, 
#  but first needs to sort in O(nlog(n)), so its overall complexity is O(nlog(n)).

#part 5
def covers(lst, segment):
    lst.sort()
    bottom,top = segment #represents the segment yet to be covered.    
    for start,end in lst: 
        if start>bottom:
            return False
        if  end >= bottom:
            bottom = end
            if bottom>=top:
                return True
    return False

for i in range()