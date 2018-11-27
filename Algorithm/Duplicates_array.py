# Question 4 Duplicates in one dimensional array
# Problem is that we want to find duplicates in one dimensional array of integers
# Integer values are smaller than the length of the array


def duplicates(nums):
    for num in nums:

        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print("Repetition Found:", abs(num))


nums = [2,3,5,1,4,3,2]
duplicates(nums)
