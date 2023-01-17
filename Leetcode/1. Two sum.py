"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

nums = [2, 7, 11, 15]
target = 26


def twoSum(nums, target):
    res = []
    for num in nums:
        for ind in range(nums.index(num)+1, len(nums)):
            if target == num + nums[ind]:
                res += [nums.index(num), ind]
                return res


print('twoSum', twoSum(nums, target))


def twoSum_I(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
            return [seen[remaining], i]  # 4
        else:
            seen[value] = i


print('twoSum_I', twoSum_I(nums, target))


def twoSum_II(numbers, target):
    # for left in range(len(numbers) - 1):  # 1
    left = 0
    right = len(numbers) - 1  # 2
    while left < right:  # 3
        temp_sum = numbers[left] + numbers[right]  # 4
        if temp_sum > target:  # 5
            right -= 1  # 6
        elif temp_sum < target:  # 7
            left += 1  # 8
        else:
            return [left, right]  # 9


print('twoSum_II', twoSum_II(nums, target))
