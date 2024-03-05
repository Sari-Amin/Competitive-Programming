class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        for br in s:
            
            if br == ")":
                if stack and stack[-1] != "(":
                    temp = stack.pop() * 2
                    stack.pop()
                
                    if stack and stack[-1] != "(":
                        temp += stack.pop()

                    stack.append(temp)
                elif stack and stack[-1] == "(":
                    stack.pop()
                    if stack and stack[-1] != "(":
                        temp = stack.pop() + 1
                        stack.append(temp)
                    else:
                        stack.append(1)

            else:
                stack.append(br)

        return stack[-1]
