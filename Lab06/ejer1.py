def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    n = len(nums)
    result = []
    window = []  

    for i in range(n):
        # Remove indices outside the window
        if window and window[0] < i - k + 1:
            window.pop(0)

        # Remove elements smaller than current from the end
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Add current index
        window.append(i)

        # Append max value to result once the first window is ready
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Test Cases
print('Ejemplo: ', max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

print(max_sliding_window([4, 2, 12, 3, 8], 2))

print(max_sliding_window([1], 1))

