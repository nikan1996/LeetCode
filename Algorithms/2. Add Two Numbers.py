#!/usr/bin/env python
# encoding: utf-8
"""
    @author:nikan(859905874@qq.com)
    @file: 2. Add Two Numbers.py
    
    ~~~~~~~~~~~
    :license: MIT, see LICENSE for more details.
    @time: 31/01/2018 2:47 PM
"""
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        currentNode = l3
        quotient = 0
        while l1 or l2:
            value = quotient
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            quotient = value // 10
            value = value % 10
            currentNode.next = ListNode(value)
            currentNode = currentNode.next
            if quotient:
                currentNode.next = ListNode(quotient)
        return l3.next





