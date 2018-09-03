###########################################################################
# FILE : ex6.py
# WRITERS : Yosef Yehoshua , yosef12345 , 302818513
# EXERCISE : intro2cs ex7 2015­2016
# DESCRIPTION: A program that practice programming with recursion.
###########################################################################


STR_NUM1 = '0'
STR_NUM2 = '1'
EMPTY_SRT = ''


def print_to_n(n):
    """
    prints integers in arising order from 1 to n
    :param n: integer bigger than -1
    :return: a print of all integers smaller than n till 1
    """
    if n > 0:
        if n == 0:
            return None
        else:
            print_to_n(n-1)
        print(n)
    else:
        return None




def print_reversed_n(n):
    """
    prints integers in decreasing order from n to 1
    :param n: integer bigger than 0
    :return: a print of all integers smaller than n till 1
    """
    if n > 0:
        print(n)
        if n == 0:
            return None
        else:
            print_reversed_n(n-1)
    else:
        return None


def has_divisor_smaller_than(n, i):
    """
    returns True/False if there is a divisor for n that smaller than i
    :param n: integer- the number to find the divisor from
    :param i:integer - the boundary number
    :return: True/False
    """
    if i == 1 or i <= 0:
        return False
    elif n % i == 0 and n != i:
        return True
    else:
        return has_divisor_smaller_than(n, i-1)


def is_prime(n):
    """
    returns a bool value if n is a prime number, using
    has_divisor_smaller_than
    :param n: integer
    :return: True/False
    """
    prime = has_divisor_smaller_than(n, n)
    if n > 1 and prime is False:
        return True
    else:
        return False


def list_of_divisor_smaller_than(n, i, divisor_list=[]):
    """
    return a list of the divisors of a given n that are smaller that i
    :param n: integer
    :param i: integer
    :param divisor_list: list of divisors of n from i
    :return: all of n divisors from i and under
    """
    n = abs(n)
    i = abs(i)
    if n == 1 and i != 0:
        divisor_list.append(1)
        return divisor_list
    if n == 0:
        return None
    if i == 0:
        return
    elif n % i == 0 and i > 0:
        divisor_list.append(i)
    list_of_divisor_smaller_than(n, i-1, divisor_list)
    return divisor_list


def divisors(n):
    """
    uses list_of_divisor_smaller_than to find all of the divisors of n
    :param n: integer
    :return: list of integers - n divisors
    """
    if n != 0:
        divisors_list = list_of_divisor_smaller_than(n, n, divisor_list=[])
        divisors_list.reverse()
        return divisors_list
    else:
        return []


def factorial(n):
    """
    calculate n factorial
    :param n: a number
    :return: n factorial
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def exp_n_x(n, x):
    """
    calculate the sum of the exp. expiration '(x^n)/n' as x is the power base
     and n is the power & and sum boundary
    :param n: power & and sum boundary
    :param x: power base
    :return: float - the sum of the expiration
    """
    if n == 0:
        if x != 0:
            return 1
        else:
            return None
    elif x == 0:
        return 1
    return (float(x)**n)/factorial(n) + exp_n_x(n-1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    solves 'Hanoi Towers' game using its famous algorithm
    (for more detiles visit https://en.wikipedia.org/wiki/Tower_of_Hanoi)
    :param hanoi: object - the graphic game that changes
    :param n: int - number of discs in the game
    :param src: object - the initial peg
    :param dest: object - the peg to move a single disc to
    :param temp: object - temporary peg to move a disc to
    """
    if n >= 1:
        if n == 1:
            hanoi.move(src, dest)
        else:
            play_hanoi(hanoi, n-1, src, temp, dest)
            play_hanoi(hanoi, 1, src, dest, temp)
            play_hanoi(hanoi, n-1, temp, dest, src)
    else:
        return


def print_binary_sequences_with_prefix(prefix, n):
    """
    prints strings with all the possibilities in len 'n' and under prefix
    condition.
    :param prefix: '0'/'1' - a branch, that starts from prefix.
    :param n: integer len of number of possibility
    :return: print strings - with all the combinations of '0' & '1' under
    condition prefix.
    """
    if len(prefix) == n:
        print(prefix)
    else:
        print_binary_sequences_with_prefix(prefix + STR_NUM1, n)
        print_binary_sequences_with_prefix(prefix + STR_NUM2, n)


def print_binary_sequences(n):
    """
    calls print_binary_sequences_with_prefix function
    :param n: integer len of number of possibility
    :return: print strings - with all the combinations of '0' & '1'
    """
    print_binary_sequences_with_prefix(EMPTY_SRT, n)


def print_sequences_helper(prefix, char_list, n):
    """
    prints strings with all the possibilities in len 'n' of the values in
    char_lists that starts under prefix condition.
    :param prefix: a branch of arrangements of chars in char
    _list, that starts from prefix.
    :param char_list: list of values
    :param n: integer - len of number of possibility
    :return: print strings - with all the combinations of chars in char_list
    under condition prefix.
    """
    if len(prefix) == n:
        print(prefix)
    else:
        for i in range(len(char_list)):
            print_sequences_helper(prefix + char_list[i], char_list, n)


def print_sequences(char_list, n):
    """
    calls print_sequences_helper function.
    :param char_list: list of values
    :param n: integer - len of number of possibility
    :return: all the combinations of chars in char_list of len 'n'.
    """
    print_sequences_helper('', char_list, n)


def print_no_repetition_sequences_helper(prefix, char_list, n):
    """
    prints all sequences of chars in char_list without repetition from prefix
    condition and beyond.
    :param prefix: a branch of arrangements of chars in char
    :param char_list: a list of chars
    :param n: integer - len of number of possibility
    :return: prints all combinations of char in char list without repetition &
     under prefix condition.
    """
    if len(prefix) == n:
        print(prefix)
    else:
        for i in range(len(char_list)):
            if char_list[i] not in prefix:
                print_no_repetition_sequences_helper(prefix + char_list[i],
                                                     char_list, n)


def print_no_repetition_sequences(char_list, n):
    """
    calls print_no_repetition_sequences_helper and prints all the combinations
    of char_list's chars without repetition.
    :param char_list: list of chars
    :param n: integer - len of number of possibility
    :return: prints all the combinations of char_list's chars without
    repetition.
    """
    print_no_repetition_sequences_helper('', char_list, n)


def no_repetition_sequences_list_helper(sequences_list, prefix,
                                        char_list, n):
    """
    returns a list of all sequences of chars in char_list without repetition
    from prefix condition and beyond.
    :param sequences_list:  list of all sequences of chars in char_list
    without repetition.
    :param prefix: a branch of arrangements of chars in char
    :param char_list: a list of chars
    :param n: integer - len of number of possibility
    :return: sequences_list
    """
    if len(prefix) == n:
        sequences_list.append(prefix)
        return prefix
    else:
        for i in range(len(char_list)):
            if str(char_list[i]) not in prefix:
                no_repetition_sequences_list_helper(
                    sequences_list, prefix + str(char_list[i]), char_list, n)
    return sequences_list


def no_repetition_sequences_list(char_list, n):
    """
    calls no_repetition_sequences_list_helper function.
    :param char_list: a list of chars
    :param n:  integer - len of number of possibility
    :return: sequences_list -list of all sequences of chars in char_list
    without repetition.
    """
    if n > 0:
        sequences_list = []
        prefix = ''
        return no_repetition_sequences_list_helper(sequences_list,
                                                   prefix, char_list, n)
    else:
        return ['']
