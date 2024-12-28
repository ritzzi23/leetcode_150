from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        sorted_dict = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)

        top_k = list(sorted_dict.keys())[:k]
        return print(top_k)


        
a = Solution()
a.topKFrequent(nums = [1,2,2,3,3,3], k = 2)

