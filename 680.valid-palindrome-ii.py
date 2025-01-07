#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (41.95%)
# Likes:    8404
# Dislikes: 464
# Total Accepted:    861K
# Total Submissions: 2.1M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # create a new function for checking without removing any characters
        # then after the first removing happens, we let it recursive.
        def isPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                elif left == right or left + 1 == right:
                    return True
                else:
                    left += 1
                    right -= 1
                
            return False
        
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return isPalindrome(left, right-1) or isPalindrome(left+1, right)
            elif left == right or left + 1 == right:
                return True
            else:
                left += 1
                right -= 1
        
        return False


# @lc code=end

