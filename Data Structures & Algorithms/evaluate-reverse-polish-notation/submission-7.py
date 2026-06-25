class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-/*"
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                print(stack, tokens[i])
                evaled = 0
                first = int(stack.pop())
                second = int(stack.pop())

                if tokens[i] == "+":
                    evaled = first + second
                elif tokens[i] == "-":
                    evaled = second - first
                elif tokens[i] == "*":
                    evaled = second * first
                elif tokens[i] == "/":
                    evaled = second / first
                print(evaled)
                stack.append(evaled)
        
        return int(stack.pop())