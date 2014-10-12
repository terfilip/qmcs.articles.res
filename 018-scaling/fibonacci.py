#!/usr/bin/env python3

from sys import argv

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate(argv):
    alg = int(argv[1])
    n = int(argv[2])
    if alg == 1:
        print("The {}th Fibonacci number is: {}".format(n,fib1(n)))
    elif alg == 2:
        print("The {}th Fibonacci number is: {}".format(n,fib2(n)))
    else:
        raise ValueError("Usage: ./fibonacci.py {algorithm(1 or 2)} {nth Fibonacci number}")

if __name__ == '__main__':
    calculate(argv)
