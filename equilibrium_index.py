def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1  # No equilibrium index found

# Example usage
if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]
    index = find_equilibrium_index(arr)
    print(f'Equilibrium Index: {index}')