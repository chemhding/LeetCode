#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (45.63%)
# Likes:    21199
# Dislikes: 550
# Total Accepted:    2.4M
# Total Submissions: 5.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums)
        found = False
        
        while left < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                found = True
                break

        if found:
            left = mid
            right = mid
            # make sure left and right does not have boundary problems
            # i.e. input: [1], 1, output [0,0]
            while left > 0 and nums[left-1] == nums[left]:
                left -= 1
            while right < len(nums) -1 and nums[right] == nums[right+1]:
                right += 1
            return [left, right]
        else:
            return [-1, -1]

        
            
    
        
# @lc code=end

