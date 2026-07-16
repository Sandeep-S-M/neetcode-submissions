class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in ['+','-','*','/']:
                x = int(stack.pop())
                y = int(stack.pop())
                match ch:
                    case '+':stack.append(y+x)
                    case '-': stack.append(y-x)
                    case '*': stack.append(y*x)
                    case '/':stack.append(int(y/x))
            else:
                stack.append(int(ch))
        return stack.pop()
                    