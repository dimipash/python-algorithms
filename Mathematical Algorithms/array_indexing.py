# 2D to 1D Array Indexing Algorithm

def index_2d_to_1d(row, col, num_cols):
    """
    Convert 2D array coordinates to a 1D array index.
    
    This function demonstrates how to map a 2D array position 
    to its equivalent index in a flattened 1D array.
    
    Parameters:
    - row: The row number in the 2D array (zero-indexed)
    - col: The column number in the 2D array (zero-indexed)
    - num_cols: Total number of columns in the original 2D array
    
    Returns:
    - The corresponding 1D array index
    """
    # The formula: 1D index = row * total number of columns + column
    return row * num_cols + col

def demonstrate_2d_to_1d_indexing():
    """
    Demonstrate the 2D to 1D indexing conversion with a concrete example.
    """
    # Create a sample 2D array
    sample_2d_array = [
        [0, 1, 2, 3],     # First row
        [4, 5, 6, 7],     # Second row
        [8, 9, 10, 11]    # Third row
    ]
    
    # Number of columns in the original 2D array
    num_cols = len(sample_2d_array[0])
    
    # Demonstrate conversion for a specific element
    example_row, example_col = 2, 3
    
    # Convert 2D coordinates to 1D index
    converted_index = index_2d_to_1d(example_row, example_col, num_cols)
    
    # Validate the conversion
    print("2D Array:")
    for row in sample_2d_array:
        print(row)
    
    print("\nFlattened 1D Array:")
    flattened_array = [item for sublist in sample_2d_array for item in sublist]
    print(flattened_array)
    
    print(f"\nElement at 2D position ({example_row}, {example_col}): {flattened_array[converted_index]}")
    print(f"1D index for (2, 3): {converted_index}")

def reverse_1d_to_2d(index, num_cols):
    """
    Convert a 1D array index back to 2D coordinates.
    
    This function shows how to go from a 1D index back to 2D row and column.
    
    Parameters:
    - index: The 1D array index
    - num_cols: Total number of columns in the original 2D array
    
    Returns:
    - A tuple of (row, column) coordinates
    """
    # Calculate row: integer division of index by number of columns
    row = index // num_cols
    
    # Calculate column: remainder of index divided by number of columns
    col = index % num_cols
    
    return (row, col)

def main():
    """
    Main function to showcase 2D and 1D array indexing conversions.
    """
    print("# 2D to 1D Array Indexing Demonstration #")
    
    # Demonstrate the forward conversion (2D to 1D)
    demonstrate_2d_to_1d_indexing()
    
    print("\n# Reverse Conversion (1D to 2D) Examples #")
    # Demonstrate reverse conversion with a few examples
    num_cols = 4
    test_indices = [5, 11, 7]
    
    for index in test_indices:
        row, col = reverse_1d_to_2d(index, num_cols)
        print(f"1D Index {index} corresponds to 2D coordinates: (row {row}, column {col})")

if __name__ == "__main__":
    main()