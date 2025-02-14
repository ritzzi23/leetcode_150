#A solution that runs
#  in O(n) time is trivial, 
# can you write an algorithm that runs in O(log n) time

#rotated sorted array nums are unique, return the minimum element of this array

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        
        return nums[left]


a = Solution()
print(a.findMin(nums = [4,5,0,1,2,3]))

