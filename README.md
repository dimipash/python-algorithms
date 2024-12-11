# Python Algorithms

## Equilibrium Index

### Problem Description
The equilibrium index in an array is a position where the sum of elements on the left is equal to the sum of elements on the right.

### Algorithm Explanation
1. Calculate the total sum of the array
2. Traverse the array, keeping track of left and right sums
3. At each index, check if left_sum equals right_sum
4. If a match is found, return that index
5. If no equilibrium index is found, return -1

### Time Complexity
- O(n), where n is the length of the array

### Example
```python
arr = [-7, 1, 5, 2, -4, 3, 0]
index = find_equilibrium_index(arr)  # Returns 3
```

### Implementation Details
See `equilibrium_index.py` for the full implementation.