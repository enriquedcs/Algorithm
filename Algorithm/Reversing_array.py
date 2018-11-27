# Question 1
# Reverse T[] array in 0(N) linear time
# for example input [1,2,3,4,5] output [5,4,3,2,1]

def reverse_array(nums):
    #first pointer of first item
    start_index = 0
    #last pointer of the last item
    end_index = len(nums)-1

    while end_index>start_index:
        #swap two items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        #increment first pointer
        start_index = start_index+1
        #decrement last pointer
        end_index = end_index-1

    #return list
    return nums

def reverse_eff(nums):
    nums = nums[::-1]
    return nums


nums = [1,2,3,4,5,6,7,8]

print(reverse_eff(nums))

print(reverse_array(nums))

