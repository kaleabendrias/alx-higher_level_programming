#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    for idx, num in enumerate(list_of_integers):
        left = list_of_integers[idx - 1] if idx > 0 else float('-inf')
        right = list_of_integers[idx + 1] if idx < len(list_of_integers) - 1 else float('-inf')

        if num >= left and num >= right:
            return num

