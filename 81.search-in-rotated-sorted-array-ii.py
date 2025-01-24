#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]: # cannot predict where the start is
                l += 1
            elif nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]: # meaning [mid, r] must be ascending
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # meaning [l, mid] must be ascending
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            
        return False

# @lc code=end

