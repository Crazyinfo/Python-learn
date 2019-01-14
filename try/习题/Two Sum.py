# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


# 自解
def twoSum(nums, target):
    for x in nums:
        for i in nums[ nums.index(x)+ 1 : len(nums) + 1]:
            if x + i == target:
                print(x, '+', i, '=', target)
            else:
                continue


twoSum([2, 7, 11, 15], 9)

twoSum([2, 7, 11, 15], 18)



