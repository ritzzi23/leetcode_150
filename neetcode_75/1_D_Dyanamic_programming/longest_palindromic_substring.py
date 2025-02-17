
from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_around_center(l,r):
            while l>= 0 and r < len(s) and s[l] == s[r]:
                
                l -= 1
                r += 1
            return s[l+1 :r]
        
        longest = ""

        for i in range(len(s)):
            #odd elements
            odd = expand_around_center(i,i)
            
            #even elements
            even = expand_around_center(i,i+1)
            if (len(odd) > len(longest)):
                longest = odd
            if (len(even) > len(longest)):
                longest = even
            
            

        return(longest )

        

a = Solution()
s = "ababd"
print(a.longestPalindrome(s))
