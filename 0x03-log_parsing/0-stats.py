#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""


import sys
import signal
import re


def signal_handler(sig, frame):
    """
    prints statistics and exits on CTRL+C
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """
    Prints total file size and status code counts.
    """
    print("File size:", total_size)
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def process_line(line):
    """
    Uses regular expression to extract IP, status code, and file size.
    Converts status code and file size to integers.
    Updates total size and status counts.
    """
    global total_size, status_counts, line_count

    match = re.match(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
        line)
    if match:
        _, status_code, file_size = match.groups()
        try:
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1
        except ValueError:
            pass


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    process_line(line)
    if line_count % 10 == 0:
        print_stats()
        line_count = 0

print_stats()
