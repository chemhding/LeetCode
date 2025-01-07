#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (39.70%)
# Likes:    8504
# Dislikes: 4548
# Total Accepted:    2.3M
# Total Submissions: 5.8M
# Testcase Example:  '4'
#
# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
# 
# You must not use any built-in exponent function or operator.
# 
# 
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# 
# 
# 
# Example 1:
# 
# 
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# 
# 
# Example 2:
# 
# 
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down
# to the nearest integer, 2 is returned.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # NOTE: Plus and Multiply operation could lead to stack overflow.
        # Thus, we need l+(r-l)//2 instead of (l+r)/2
        # and x/mid instead of mid * mid

        l = 0
        r = x
        mid = 0

        while l < r:
            mid = l + (r-l)//2
            if l == mid:
                return mid
            if x/mid < mid:
                r = mid
            elif x/mid == mid:
                return mid
            else:
                l = mid
        
        return mid

        
# @lc code=end

