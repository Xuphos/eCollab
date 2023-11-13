"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:
1,2,3,5,8,13,21,34,55,89,...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
https://projecteuler.net/problem=2
"""


def print_fibonacci(length):
    i = 0
    fib_list = [1, 2]
    while True:
        if i >= 8:
            break
        fib_list.append(fib_list[-2] + fib_list[-1])
        i += 1
    print(fib_list)



print_fibonacci(2)
