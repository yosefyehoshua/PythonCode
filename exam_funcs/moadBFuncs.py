# def blurg(seq):
#     a = next(seq)
#     print("a: ", a)
#     yield a
#     for b in seq:
#         print("b: ", b)
#         mid = (a+b)//2
#         a= b
#         yield mid
#         yield b
#
# my_iter = iter([0,8])
# my_blurg = blurg(blurg(my_iter))
# print(list(my_blurg))

#
# def f(x): return 2*x
#
#
#
# def aggregate(f):
#     ass = []
#     def af(x):
#         ass.append(f(x))
#         return ass
#     return af
#
# h = aggregate(f)
#
# print(h(7))
# print(h(5))
# print(h(7))
#
# def zipper(head1, head2):
# while head1:
#      next1 = head1.next
#      next2 = head2.next
#      head1.next = head2
#      head2.next = next1
#      head1 = next1
#      head2 = next2

# def ladder(n):
#     newlist = helper(n,"", [])
#     for i in newlist:
#         print(i)
#
#
# def helper(n,str1,lst1):
#     if n==0:
#         lst1.append(str1)
#         return lst1
#     if n<0:
#         return
#     helper(n-1,str1+"1",lst1)
#     helper(n-2,str1+"2",lst1)
#     helper(n-3,str1+"3",lst1)
#     helper(n-4,str1+"4",lst1)
#     return lst1
#
# ladder(4)


# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
#
# print(A0)
# print(A1)
# print(A3)
# print(A4)
# print(A5)
# print(A6)




# def help_printToK(pre,n,k):
#     if len(pre) == n or n==0:
#         temp = []
#         for item in pre:
#             temp.append(item)
#         print(temp)
#         return
#     else:
#         for i in range(k):
#             help_printToK(pre+str(i+1),n,k)
#
#
# def printToK(n,k):
#     help_printToK("",n,k)

def rec(str,n,k,lst):
    if n==0:
        for i in str:
            lst.append(str)
            print(lst)

    else:
        for i in range(k+1):
            rec(str+str(i),n-i,k,lst)


rec("",2,3,[])

