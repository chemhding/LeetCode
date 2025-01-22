#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        
        l, r = 1, n - 2

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid
            elif nums[mid] > nums[mid-1]:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# @lc code=end

