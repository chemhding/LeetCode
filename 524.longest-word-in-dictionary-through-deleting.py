#
# @lc app=leetcode id=524 lang=python
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (51.47%)
# Likes:    1815
# Dislikes: 359
# Total Accepted:    162.1K
# Total Submissions: 315K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# Given a string s and a string array dictionary, return the longest string in
# the dictionary that can be formed by deleting some of the given string
# characters. If there is more than one possible result, return the longest
# word with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# 
# Example 1:
# 
# 
# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# 
# 
# Example 2:
# 
# 
# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        def pruning(w):
            ps = len(s) - 1
            pw = len(w) - 1

            while ps >= 0 and pw >= 0:
                if w[pw] == s[ps]:
                    pw -= 1
                ps -= 1
            
            if pw >= 0:
                return False
            else:
                return True

        # first sort the dictionary by the desired order.
        dictionary = sorted(dictionary, key = lambda x: (-len(x), x))
        # then check the word one by one.
        for w in dictionary:
            if pruning(w):
                return w
            
        return ""


        
# @lc code=end

