#Question 6
# Largest sum subarray
# Algorith to find the sum of contiguos subarray


def kadane_algorith(nums):
    max_global = nums[0]
    max_current = nums[0]

    for i in range (1,len(nums)):
        max_current = max(nums[i], max_current+nums[i])

        if max_current > max_global:
            max_global = max_current

    return max_current

nums = [1,-2,3,4,-5,8]
print(kadane_algorith(nums))
