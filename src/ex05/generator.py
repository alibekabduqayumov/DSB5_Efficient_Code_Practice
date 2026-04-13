#!/usr/bin/env python3
import sys
import os
import psutil
import time


def read_file_generator(path):
    with open(path, 'r') as f:
        for line in f:
            yield line


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generator.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    process = psutil.Process(os.getpid())
    start_time = time.process_time()

    for line in read_file_generator(filepath):
        pass

    peak_memory_gb = process.memory_info().rss / (1024 ** 3)
    elapsed = time.process_time() - start_time

    print(f"Peak Memory Usage = {peak_memory_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time = {elapsed:.2f}s")


if __name__ == '__main__':
    main()