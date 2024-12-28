"""Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

"""

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(i)
        print(anagram)

        return print(list(anagram.values()))


a = Solution()
a.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"])

