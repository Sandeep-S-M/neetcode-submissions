class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for c in tokens:
            if c in ['+','*','-','/']:
                y= int(stack.pop())
                x = int(stack.pop())
                match c:
                    case '+':stack.append(x+y)
                    case '-':stack.append(x-y)
                    case '*':stack.append(x*y)
                    case '/':stack.append(int(x/y))
                    

            else:
                stack.append(int(c))
        return stack.pop()
