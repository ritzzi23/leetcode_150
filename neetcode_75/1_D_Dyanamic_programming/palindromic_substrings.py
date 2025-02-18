
from typing import List
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand_around_center(l,r, count):
            while l>= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        count = 0

        for i in range(len(s)):
            #odd elements
            count = expand_around_center(i,i,count)
            
            #even elements
            count = expand_around_center(i,i+1,count)
        return(count)

        

a = Solution()
#s = "abc"
s = "aaa"
print(a.countSubstrings(s))
