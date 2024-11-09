'''Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_prod = [1] * len(nums)
        left_prod = 1
        right_prod = 1        
        for i in range(len(nums)):
            output_prod[i] = left_prod
            left_prod *=  nums[i]
            
        print(output_prod)
        for j in range(len(nums)- 1, -1, -1):
            output_prod[j] *= right_prod

            right_prod *= nums[j]

        return output_prod        

'''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)
        result = [1] * len(nums)
        left_prod = 1
        right_prod = 1
        print(nums)

        for i in range(len(nums)):
            prefix_prod[i] = left_prod
            left_prod *=  nums[i]
            
        print(prefix_prod)
        for j in range(len(nums)- 1, -1, -1):
            suffix_prod[j] = right_prod
            right_prod *= nums[j]
            
        print(suffix_prod)

        for i in range(len(prefix_prod)):
            result[i] = (prefix_prod[i]*suffix_prod[i])
        return result'''




'''
import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            current_prod = 0
            current_elem = nums[i]
            nums.remove(current_elem)
            current_prod = math.prod(nums)
            nums.insert(i,current_elem)
            result.append(current_prod)
        return result'''
    
nums = [-1,1,0,-3,3]
a = Solution()
print(a.productExceptSelf(nums))