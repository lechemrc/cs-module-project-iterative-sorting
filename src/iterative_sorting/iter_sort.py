nums = [2, 6, 8, 3, 4, 1, 9, 6, 7]
def insert_sort(nums):
    # Loop through sums
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        # While we're not at the beginning. AND
        while j > 0 and temp < nums[j - 1]:
            # swap
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp
    return nums

print(nums)
sorted_nums = insert_sort(nums[:])
print(nums)
print(sorted_nums)