
from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        if n==1:
            return 1
        if n ==2:
            return 2

        for i in range(n-2,-1,-1):
            temp = one
            one = one + two
            two = temp 
        return one
        

a = Solution()
print(a.climbStairs(n = 2))
