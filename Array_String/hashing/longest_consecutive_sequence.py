'''
Intuition: think of as number line 
if a element is starting point it would not have a left start.
'''
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while(num + length) in numSet:
                    length += 1
                longest = max(longest,length)    
        return print(longest)    
        
        

        
            
    
a = Solution()
a.longestConsecutive(nums = [2,20,4,10,3,4,5])

