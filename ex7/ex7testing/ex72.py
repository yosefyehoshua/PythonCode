def print_to_n(n):
    print(n)
    if n==1:

        return None
    else:
        print_to_n(n-1)


def has_divisor_smaller_than(n, i):
    if i==1:
        return False

    elif n%i == 0 and n != i:
        return True

    else:
        return has_divisor_smaller_than(n, i-1)

def is_prime(n):

    if has_divisor_smaller_than(n, n):
        return False
    else:
        return True



# def flatten_list(a, result=None):
#
#     for i in range(len(a)):
#         if type(a[i]) == int:
#             result.append(a[i])
#
#         else:
#             flatten_list(a[i], result)
#
#     return result

# a = [4,[4,1],7,[3,5,1],10]
# print(flatten_list(a, []))

def flatten_dict(a, result=None):
    for key in a:
        if type(a[key]) == dict:
            temp = {}
            for key1 in a[key]:
                temp[key+"."+key1] = a[key][key1]
                flatten_dict(temp, result)
        else:
            result[key] = a[key]

    return result


a = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
print(flatten_dict(a,{}))