'''Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.'''

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        gloabal_startValue = 1
        i = 0
        while(i<len(nums)):
            if(startValue + nums[i] >= 1):
                startValue += nums[i]
                print(i,nums[i],startValue)                
                i += 1

            else:
                print(i,nums[i],startValue)                
                startValue = abs(nums[i]) + 1
                print(startValue)
                startValue += nums[i]
                print(startValue)                
                i +=1
        return startValue

nums = [-3,2,-3,4,2]
a = Solution()
print(a.minStartValue(nums))        