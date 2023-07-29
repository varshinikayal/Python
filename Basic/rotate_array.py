def rotate(nums, k):
    n = len(nums)
  # To handle cases where k is larger than the array length
    k %= n  
    nums[:] = nums[-k:] + nums[:-k]

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
