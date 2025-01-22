"""
Bogo Sort Implementation

This script implements the Bogo Sort algorithm, which sorts an array by
repeatedly shuffling it until it is sorted. It is highly inefficient and
primarily used for educational purposes to illustrate algorithmic inefficiency.

Time Complexity: O((n+1)!) on average
Space Complexity: O(1) auxiliary space
"""

import random


# Function to check if the array is sorted
def is_sorted(arr):
    """
    Checks if the array is sorted in ascending order.

    Parameters:
    arr (list): The array to check.

    Returns:
    bool: True if the array is sorted, False otherwise.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# Bogo Sort function
def bogo_sort(arr):
    """
    Sorts an array using the Bogo Sort algorithm.

    Bogo Sort works by repeatedly shuffling the array until it is sorted.
    This is highly inefficient with an average time complexity of O((n+1)!).

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    tuple: A tuple containing the sorted array and the number of attempts taken to sort it.
    """
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)  # Shuffle the array randomly
        attempts += 1
    return arr, attempts


# Example usage
if __name__ == "__main__":
    arr = [3, 2, 5, 1, 4]  # Initial unsorted array
    sorted_arr, attempts = bogo_sort(arr)  # Perform Bogo Sort
    print("Sorted array:", sorted_arr)  # Output the sorted array
    print("Attempts taken:", attempts)  # Output the number of attempts
