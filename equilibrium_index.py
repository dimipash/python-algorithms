"""
EQUILIBRIUM INDEX IN ARRAY

Repository: Python Algorithms Collection
Algorithm: Equilibrium Index Finder

Problem Description:
The equilibrium index in an array is a position where the sum of elements 
on the left is equal to the sum of elements on the right. 

Algorithm Overview:
- Efficiently find the balance point in an array
- Linear time complexity O(n)
- Returns the first equilibrium index or -1 if no such index exists

Key Steps:
1. Calculate the total sum of the array
2. Traverse the array, tracking left and right sums
3. Compare left and right sums at each index
4. Return the first index where sums match

Time Complexity: O(n)
Space Complexity: O(1)

Example:
arr = [-7, 1, 5, 2, -4, 3, 0]
Equilibrium Index: 3 (index where left and right sums are equal)
"""

def find_equilibrium_index(arr):
    """
    Find the equilibrium index in the given array.
    
    Args:
        arr (list): Input array of numbers
    
    Returns:
        int: First equilibrium index or -1 if no such index exists
    """
    total_sum = sum(arr)
    left_sum = 0
    
    for i, num in enumerate(arr):
        # Calculate right sum by subtracting left sum and current element
        right_sum = total_sum - left_sum - num
        
        # Check if left and right sums are equal
        if left_sum == right_sum:
            return i
        
        # Update left sum for next iteration
        left_sum += num
    
    return -1  # No equilibrium index found

# Example usage and demonstration
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [-7, 1, 5, 2, -4, 3, 0],  # Has an equilibrium index
        [1, 2, 3],                # No equilibrium index
        [0, 0, 0],                # Multiple possible indices
    ]
    
    for arr in test_arrays:
        index = find_equilibrium_index(arr)
        print(f"Array: {arr}")
        print(f"Equilibrium Index: {index}")
        print("-" * 30)