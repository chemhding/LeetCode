#
# @lc app=leetcode id=633 lang=python
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (36.48%)
# Likes:    3271
# Dislikes: 611
# Total Accepted:    372K
# Total Submissions: 1M
# Testcase Example:  '5'
#
# Given a non-negative integer c, decide whether there're two integers a and b
# such that a^2 + b^2 = c.
# 
# 
# Example 1:
# 
# 
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# Example 2:
# 
# 
# Input: c = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= c <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # init a and b, start b from sqrt of c
        # then move a to the right, if not work
        # move b to the left by 1 and test again.
        # NOTE: 0 is an integer.
        a = 0
        b = int(c ** 0.5)

        if a*a + b*b == c:
            return True
        
        while a*a + b*b < c and a < b:
            a += 1
            if a*a + b*b == c:
                return True
            if a*a + b*b > c:
                b -= 1
        return False
        
# @lc code=end

