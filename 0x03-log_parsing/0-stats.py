#!/usr/bin/python3
"""0. Log parsing"""
import sys


def print_stats(total_size, status_counts):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # validating and parsing line
        if len(parts) != 7:
            continue
        ip, _, date, method, url, status_code, file_size = parts

        if (method != 'GET' or url != '/projects/260' or 
                not status_code.isdigit() or not file_size.isdigit()):
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        if status_code in status_counts:
            status_counts[status_code] += 1

        total_size += file_size

        # Print statistics from the beginning
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

# Print final stats
print_stats(total_size, status_counts)
