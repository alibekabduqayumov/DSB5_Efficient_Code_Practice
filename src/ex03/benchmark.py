#!/usr/bin/env python3
import timeit
import sys
from functools import reduce


def loop(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i * i
    return total


def reduce_func(n):
    return reduce(lambda acc, i: acc + i * i, range(1, n + 1), 0)


FUNCTIONS = {
    'loop': loop,
    'reduce': reduce_func,
}


def main():
    if len(sys.argv) != 4:
        print("Usage: ./benchmark.py <function_name> <number_of_calls> <number>")
        print(f"Available functions: {', '.join(FUNCTIONS.keys())}")
        sys.exit(1)

    func_name = sys.argv[1]
    try:
        calls = int(sys.argv[2])
        number = int(sys.argv[3])
    except ValueError:
        print("Error: number_of_calls and number must be integers")
        sys.exit(1)

    if func_name not in FUNCTIONS:
        print(f"Error: unknown function '{func_name}'. Choose from: {', '.join(FUNCTIONS.keys())}")
        sys.exit(1)

    func = FUNCTIONS[func_name]
    t = timeit.timeit(lambda: func(number), number=calls)
    print(round(t, 9))


if __name__ == '__main__':
    main()
