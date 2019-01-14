'''
给定一个String类型数组，要求写一个方法，返回数组中这些字符串的最长公共前缀。举个例子：假如数组为["123","12","4"]，经过这个方法返回的结果就应该是""。
因为"123"，"12"，"4"并没有共同的前缀，虽然"123"，"12"的公共最长前缀是"12"，但是这个公共前缀"12"与"4"没有公共前缀，所以最后返回的结果就是""。
最简单的思路就是将str[0]，当作临时最长公共前缀，然后用这个前缀依次和剩下的字符串进行前缀比较，都比较完后，就将最后得到的最新公共最长前缀返回即可。
'''
# Write a function to find the longest common prefix string amongst an array of strings.
# 网摘
def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)): # zip(strs)=['sssss','ddddd','dfgff']
        if len(set(letter_group)) > 1: # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
            return strs[0][:i]
    else:
        return min(strs)

print(longestCommonPrefix(['sdd','sdf','sdg','sdfasgfdhsdg','sdfsa']))

print(min("safadf"))  # 返回字符串中最小的字母。

