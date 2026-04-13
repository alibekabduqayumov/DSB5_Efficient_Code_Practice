#!/usr/bin/env python3
import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
          'anna@live.com', 'philipp@gmail.com'] * 5


def loop(emails_list):
    result = []
    for email in emails_list:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result


def list_comprehension(emails_list):
    return [email for email in emails_list if email.endswith('@gmail.com')]


def map_func(emails_list):
    return list(map(lambda e: e, filter(lambda e: e.endswith('@gmail.com'), emails_list)))


def filter_func(emails_list):
    return list(filter(lambda e: e.endswith('@gmail.com'), emails_list))


FUNCTIONS = {
    'loop': loop,
    'list_comprehension': list_comprehension,
    'map': map_func,
    'filter': filter_func,
}


def main():
    if len(sys.argv) != 3:
        print("Usage: ./benchmark.py <function_name> <number_of_calls>")
        print(f"Available functions: {', '.join(FUNCTIONS.keys())}")
        sys.exit(1)

    func_name = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("Error: number_of_calls must be an integer")
        sys.exit(1)

    if func_name not in FUNCTIONS:
        print(f"Error: unknown function '{func_name}'. Choose from: {', '.join(FUNCTIONS.keys())}")
        sys.exit(1)

    func = FUNCTIONS[func_name]
    t = timeit.timeit(lambda: func(emails), number=n)
    print(round(t, 9))


if __name__ == '__main__':
    main()
