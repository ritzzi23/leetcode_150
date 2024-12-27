from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = 0
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = left_sum
            left_sum += nums[i]
        print(answer)
        for j in range(len(nums)-1, -1, -1):
            answer[j] = abs(answer[j] - right_sum)
            right_sum += nums[j]
        return answer

nums = [10,4,8,3]
a = Solution()
print(a.leftRightDifference(nums))        