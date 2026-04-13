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


def map_approach():
    return list(map(lambda e: e, filter(lambda e: e.endswith('@gmail.com'), emails)))


def main():
    n = 90_000_000
    t_loop = timeit.timeit(loop_approach, number=n)
    t_comp = timeit.timeit(list_comprehension_approach, number=n)
    t_map = timeit.timeit(map_approach, number=n)

    times = sorted([(t_loop, "loop"), (t_comp, "list comprehension"), (t_map, "map")])
    best = times[0][1]
    print(f"it is better to use a {best}")
    print(" vs ".join(str(t) for t, _ in times))


if __name__ == '__main__':
    main()
