class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for c in tokens:
            if c == "+":
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif c == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif c == "*":
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif c == "/":
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(c))

        return stack.pop()
