#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (43.86%)
# Likes:    4806
# Dislikes: 500
# Total Accepted:    502.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3,5]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might
# become:
# 
# 
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# 
# 
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# 
# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.
# 
# You must decrease the overall operation steps as much as possible.
# 
# 
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
# 
# 
# 
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates. Would this affect the runtime complexity?
# How and why?
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the right end cannot be larger than the left point if there's valid rotation exist.
        l, r = 0, len(nums) -1

        while l <= r:
            if l == r:
                return nums[l]
            mid = l + (r-l)//2
            if nums[mid] > nums[r]: # the start point must be in the right part
                l = mid + 1
            # can be more specific and create more if else inside this condition
            # but for simplicity I think this is better.
            elif nums[mid] == nums[r]: 
                r -= 1
            else:
                r = mid


        # initial version
        # while l <= r:
        #     mid = l + (r-l)//2
        #     if l == r:
        #         return nums[l]
        #     if nums[l] <= nums[mid] and nums[mid] < nums[r]:
        #         return nums[l]
        #     if nums[l] < nums[mid] and nums[mid] <= nums[r]:
        #         return nums[l]

        #     if nums[l] == nums[mid] and nums[r] < nums[mid]:
        #         l = mid + 1
        #     elif nums[l] == nums[mid] and nums[r] > nums[mid]:
        #         r = mid
        #     elif nums[l] == nums[mid] and nums[r] == nums[mid]:
        #         if l == r - 1:
        #             return nums[l]
        #         if nums[l] >= nums[l+1]:
        #             l += 1
        #         if nums[r] >= nums[r-1]:
        #             r -= 1
        #     elif nums[l] > nums[mid]:
        #         r = mid
        #     else:
        #         l = mid
        
# @lc code=end

