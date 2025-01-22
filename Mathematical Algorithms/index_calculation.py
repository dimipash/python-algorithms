"""
Index Calculation Implementations

Provides various methods for calculating indices in different contexts:
- Array indexing (1D and 2D)
- Image processing coordinates
- Hash table indexing
- Binary search indexing

Time Complexity: Varies by operation
Space Complexity: O(1) for calculations
"""


def calculate_1d_index(n: int) -> int:
    """Calculate index for 1D array access."""
    return n - 1


def calculate_2d_index(
    row: int, col: int, num_cols: int, row_major: bool = True
) -> int:
    """Calculate linear index for 2D array."""
    if row_major:
        return row * num_cols + col
    return col * num_cols + row


def hash_function(key: str, size: int) -> int:
    """Calculate hash table index."""
    return hash(key) % size


def binary_search(arr: list, target: int) -> int:
    """Find index using binary search."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    # 1D array example
    arr = [10, 20, 30, 40, 50]
    n = 3
    index_1d = calculate_1d_index(n)
    print(f"1D array: Element at index {index_1d} is {arr[index_1d]}")[1]

    # 2D array example
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row, col = 1, 2
    index_2d = calculate_2d_index(row, col, len(matrix[0]))
    print(f"2D array: Element at index {index_2d} is {matrix[row][col]}")[2]

    # Image processing example
    image = np.array(
        [[255, 0, 255, 0], [0, 255, 0, 255], [255, 255, 0, 0], [0, 0, 255, 255]]
    )
    x, y = 2, 1
    pixel_value = image[x, y]
    print(f"Image pixel at ({x},{y}) is {pixel_value}")[3]

    # Binary search example
    sorted_arr = [1, 2, 3, 4, 5]
    target = 3
    search_index = binary_search(sorted_arr, target)
    print(f"Binary search found target {target} at index {search_index}")[4]


if __name__ == "__main__":
    main()
