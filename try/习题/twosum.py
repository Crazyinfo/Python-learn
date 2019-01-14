# 网摘
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return [dic[target - num], i]
        dic[num] = i

m = twoSum([2, 7, 11, 15], 9)
print(m)
print(twoSum([2, 7, 11, 15], 18))