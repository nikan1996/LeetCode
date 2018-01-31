#!/usr/bin/env python
# encoding: utf-8
"""
    @author:nikan(859905874@qq.com)
    @file: 1.Two Sum.py
    
    ~~~~~~~~~~~
    :license: MIT, see LICENSE for more details.
    @time: 31/01/2018 1:26 PM
"""
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """通过构造一个 dict 来使得第二个数字的查询达到最好 O(1)的时间复杂度
        Time Complexity: O(n)
        Space Complaxity: O(1)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = dict((v, k) for k, v in enumerate(nums))
        for index, value in enumerate(nums):
            """如果遍历 num_map来获取第一个数的下标， 对于重复数字的列表，如[3,3]，得到 num_map{3:1},会导致错误，因此遍历 nums 列表是正确的做法。"""
            another = target - value
            another_index = num_map.get(another)
            if another_index:
                return [index, another_index]
        else:
            return None