class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(num1, operator, num2):
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            else:
                return int(num1 / num2)

        stack = []

        for ch in tokens:
            if ch in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(helper(num2, ch, num1))
            else:
                stack.append(int(ch))


        return stack[0]