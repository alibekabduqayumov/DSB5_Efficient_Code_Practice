#!/usr/bin/env python3
import timeit
import random
from collections import Counter

# Generate 1 million random values from 0 to 100
data = [random.randint(0, 100) for _ in range(1_000_000)]


def my_count(lst):
    counts = {}
    for val in lst:
        counts[val] = counts.get(val, 0) + 1
    return counts


def counter_count(lst):
    return dict(Counter(lst))


def my_top(lst):
    counts = my_count(lst)
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_items[:10])


def counter_top(lst):
    return dict(Counter(lst).most_common(10))


def main():
    n = 100

    t_my_count = timeit.timeit(lambda: my_count(data), number=n)
    t_counter_count = timeit.timeit(lambda: counter_count(data), number=n)
    t_my_top = timeit.timeit(lambda: my_top(data), number=n)
    t_counter_top = timeit.timeit(lambda: counter_top(data), number=n)

    print(f"my function: {round(t_my_count, 7)}")
    print(f"Counter: {round(t_counter_count, 7)}")
    print(f"my top: {round(t_my_top, 7)}")
    print(f"Counter's top: {round(t_counter_top, 7)}")


if __name__ == '__main__':
    main()
