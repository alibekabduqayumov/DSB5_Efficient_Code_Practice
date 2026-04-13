#!/usr/bin/env python3
import sys
import os
import psutil
import time


def read_file(path):
    with open(path, 'r') as f:
        return f.readlines()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ordinary.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    process = psutil.Process(os.getpid())
    start_time = time.process_time()

    lines = read_file(filepath)
    for line in lines:
        pass

    peak_memory_gb = process.memory_info().rss / (1024 ** 3)
    elapsed = time.process_time() - start_time

    print(f"Peak Memory Usage = {peak_memory_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time = {elapsed:.2f}s")


if __name__ == '__main__':
    main()