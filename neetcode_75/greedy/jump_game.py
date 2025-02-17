
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        #print(goal)

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
                #print(goal)
        return True if goal== 0 else False

a = Solution()
nums = [1,2,0,1,0]
print(a.canJump(nums))
