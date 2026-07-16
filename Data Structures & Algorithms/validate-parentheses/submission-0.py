class Solution:
    def isValid(self, s: str) -> bool:
        prev = {']':'[','}':'{',')':'('}
        stack = []
        for ch in s:
            if ch in prev:
                if not stack or stack.pop() != prev[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0


            

        