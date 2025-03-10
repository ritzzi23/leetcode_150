from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        max_profit = 0
        while right < (len(prices)):
            if (prices[right]>prices[left]):
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return int(max_profit)


        
        
        
        


a = Solution()
prices = [10,1,5,6,7,1]
print(a.maxProfit(prices))

