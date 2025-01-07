#
# @lc app=leetcode id=340 lang=python
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
#
# Given a string s and an integer k, return the length of the longest 
# substring of s that contains at most k distinct characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while len(count.keys()) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del[s[left]]
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len



# @lc code=end