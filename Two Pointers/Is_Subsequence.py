'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
 of the characters without disturbing the relative positions of the remaining characters. 
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_pointer = 0
        s_pointer = 0
        while(s_pointer< len(s) and t_pointer <len(t)):
            if (t[t_pointer] == s[s_pointer]) :
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1
        if s_pointer == len(s):
            return True
        else:
            return False

a = Solution()
s = "abc"
t = "ahbgdc"
#s = "axc" 
#t = "ahbgdc"
print(a.isSubsequence(s, t))
