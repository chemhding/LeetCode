#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (59.26%)
# Likes:    11716
# Dislikes: 206
# Total Accepted:    824.7K
# Total Submissions: 1.4M
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# 
# Return the single element that appears only once.
# 
# Your solution must run in O(log n) time and O(1) space.
# 
# 
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums)-1

        # if there's no single value, the odd index element must be the same with its previous element.
        while l <= r:
            mid = l + (r-l)//2
            # check if mid is odd, if not we decrease it by 1
            if mid % 2 == 0:
                mid -= 1
            # when it finally gets to the case [a, b], mid will be less than left
            if l == r or mid < l:
                return nums[l]
            if nums[mid] == nums[mid-1]:
                l = mid + 1
            else:
                r = mid

        # initial verision
        # while l <= r:
        #     mid = l + (r-l)//2
        #     if l == r:
        #         return nums[l]
        #     if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
        #         return nums[mid]
        #     if nums[mid] == nums[mid-1]:
        #         if mid % 2 == 0:
        #             r = mid - 2
        #         else:
        #             l = mid + 1
        #     if nums[mid] == nums[mid+1]:
        #         if mid % 2 == 0:
        #             l = mid + 2
        #         else:
        #             r = mid - 1 
        
# @lc code=end

