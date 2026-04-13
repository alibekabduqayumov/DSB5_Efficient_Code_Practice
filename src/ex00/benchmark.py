#!/usr/bin/env python3
import timeit

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
          'anna@live.com', 'philipp@gmail.com'] * 5


def loop_approach():
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result


def list_comprehension_approach():
    return [email for email in emails if email.endswith('@gmail.com')]


def main():
    n = 90_000_000
    t_loop = timeit.timeit(loop_approach, number=n)
    t_comp = timeit.timeit(list_comprehension_approach, number=n)

    if t_comp <= t_loop:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    times = sorted([t_loop, t_comp])
    print(f"{times[0]} vs {times[1]}")


if __name__ == '__main__':
    main()
