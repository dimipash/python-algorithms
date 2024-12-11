"""
Find Triplets with Zero Sum

Problem Statement:
The problem is to find all unique triplets in an array that sum to zero.
Given an array of integers, the task is to find triplets (three numbers) whose
sum is zero. These triplets should be distinct, meaning the same
combination of numbers should not appear more than once.

Algorithm:
1. Sort the array to make it easier to find unique triplets.
2. For each element in the array, use two pointers (left and right) to find
   the remaining two numbers such that their sum with the current
   element equals zero.
3. Skip duplicates to ensure no repeated triplets are added to the result.

Time Complexity: O(n^2)
Space Complexity: O(1) (excluding the space for storing output)

Example:
    Input: [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
"""

def find_triplets_with_zero_sum(arr):
    """
    Finds all unique triplets in the given array that sum to zero.

    Args:
        arr (list): Input list of integers

    Returns:
        list: List of unique triplets that sum to zero
    """
    # Sort the array to help with finding unique triplets and to use two-pointer approach
    arr.sort()
    
    # List to store zero-sum triplets
    triplets = []
    
    # Iterate through the array, leaving space for two more elements
    for i in range(len(arr) - 2):
        # Skip duplicate values to prevent repeated triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        # Initialize two pointers: one after current element, one at the end
        left, right = i + 1, len(arr) - 1
        
        while left < right:
            # Calculate current sum of three elements
            s = arr[i] + arr[left] + arr[right]
            
            # If sum is zero, we found a triplet
            if s == 0:
                # Add the current triplet to results
                triplets.append([arr[i], arr[left], arr[right]])
                
                # Move pointers and skip duplicates
                left += 1
                right -= 1
                
                # Skip duplicate left values
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                
                # Skip duplicate right values
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            
            # If sum is less than zero, move left pointer to increase sum
            elif s < 0:
                left += 1
            
            # If sum is greater than zero, move right pointer to decrease sum
            else:
                right -= 1
    
    return triplets


# Example usage
def main():
    """Demonstrate the find_triplets_with_zero_sum function."""
    arr = [-1, 0, 1, 2, -1, -4]
    result = find_triplets_with_zero_sum(arr)
    print("Input array:", arr)
    print("Triplets with zero sum:", result)


if __name__ == "__main__":
    main()