#!/usr/bin/env python
# encoding: utf-8
"""
    @author:nikan(859905874@qq.com)
    @file: 3. Longest Substring Without Repeating Characters.py
    
    ~~~~~~~~~~~
    :license: MIT, see LICENSE for more details.
    @time: 31/01/2018 3:35 PM
"""
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """找出最长的子串长度（其中子串不能含有重复字符） 滑窗法1
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sub_start_index = 0
        sub_end_index = 0
        max_len = 0
        sub_string_set = set()  # set 判断 新字符是否在子串中， O(1)的平均复杂度
        len_s = len(s)
        while sub_end_index < len_s:
            if s[sub_end_index] in sub_string_set:
                sub_string_set.remove(s[sub_start_index])
                max_len = max(max_len, sub_end_index - sub_start_index)
                sub_start_index += 1
            else:
                sub_string_set.add(s[sub_end_index])
                sub_end_index += 1
        
        return max_len


def lengthOfLongestSubstring2(self, s):
    """找出最长的子串长度（其中子串不能含有重复字符） 滑窗法2
    :type s: str
    :rtype: int
    """
    sub_start_index = -1
    max_len = 0
    sub_string_dict = {}  # dict 判断 新字符是否在子串中， dict: key <- char_index, value <- char
    for index, value in enumerate(s):
        if value in sub_string_dict:
            if sub_string_dict[value] > sub_start_index:
                sub_start_index = sub_string_dict[value]
        sub_string_dict[value] = index
        max_len = max(max_len, index - sub_start_index)
    return max_len

