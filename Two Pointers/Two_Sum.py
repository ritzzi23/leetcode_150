'''Basic Implementation of 2Sum '''

'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

'''code:'''

'Note: you may not use the same element twice'

#Brute_force:
class Solution:
    def twoSum_brute_force(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i,len(nums)):
                current_sum = nums[i] + nums[j]
                if (target == current_sum):
                    return [i+1,j+1]
                
#Dictionary_Approach:
    def twoSum_dictionary_approach(self, nums: list[int], target: int) -> list[int]:
        nums_maps = dict()
        for index, elem in enumerate(nums):
            remaining = target - elem 

            if remaining in nums_maps:
                return nums_maps[remaining]+1, index+1
            nums_maps[elem] = index

#Two_pointer_Approach:
    def twoSum_two_pointer_approach(self, nums: list[int], target: int) -> list[int]:
        num_index_list = [(index, elem) for index, elem in enumerate(nums)]
        num_index_list.sort(key=lambda x: x[1])
        left = 0
        right = len(nums) - 1

        while(left != right):
            current_sum = num_index_list[left][1] + num_index_list[right][1]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return num_index_list[left][0] + 1, num_index_list[right][0] + 1



    
a = Solution()
numbers = [2,3,4] 
target = 6
#print(a.twoSum_brute_force(numbers, target))
#print(a.twoSum_dictionary_approach(numbers, target))
print(a.twoSum_two_pointer_approach(numbers, target))


