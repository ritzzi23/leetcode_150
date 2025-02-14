"""You are given a string s consisting of the 
following characters: '(', ')', '{', '}', '[' and ']'.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')':'(','}':'{',']':'['}
        stack = []

        for c in s:
            if c in hash_map:
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                #print(stack)
        return True if not stack else False
        


a = Solution()
a.isValid(s = "([{}])")

