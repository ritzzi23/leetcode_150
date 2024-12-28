'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # because sorted that's why repeating characters would come continously 
                continue

            j = i+1
            k = len(nums)-1

            while(j<k):
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum < 0:
                    j += 1
                elif current_sum >0:
                    k -= 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    
                    while j< k and nums[j] == nums[j+1]:
                        j += 1
                    while j< k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result
    
    def threeSum_just_one_check_keeping_two_arguments_fixed(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # because sorted that's why repeating characters would come continously 
                continue

            j = i+1
            k = len(nums)-1

            while(j<k):
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum < 0:
                    j += 1
                elif current_sum >0:
                    k -= 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1

                    while j< k and nums[j] == nums[j+1]: 
                        j += 1

        return result

#------------------------------------------------    
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = []
        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1  # Two pointers
            
            while(j<k):
                current_sum = nums[i] + nums[j] + nums[k]
                if(current_sum < 0):
                    j += 1
                elif(current_sum > 0):
                    k -= 1
                else:
                    d.append([nums[i], nums[j], nums[k]])
                    # Skip duplicates for the second number
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # Skip duplicates for the third number
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return d

a = Solution()
nums = [-1,0,1,2,-1,-4]
c = list(a.threeSum(nums))
print(c)



        