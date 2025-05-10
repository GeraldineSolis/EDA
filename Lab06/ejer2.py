def rotate_array(nums, k):
    if not nums or k == 0:
        return nums

    n = len(nums)
    k = k % n  

    # Perform rotation by slicing
    rotated = nums[-k:] + nums[:-k]
    return rotated

# Test Cases
print(rotate_array([1,2,3,4,5,6,7], 3))

print(rotate_array([10, 20, 30, 40], 2))

print(rotate_array([1, 2, 3], 4))

print(rotate_array([], 5))

