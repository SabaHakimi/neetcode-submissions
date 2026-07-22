class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operands come before operator
        # push to stack until operator
        # compute, then push again
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif tokens[i] == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif tokens[i] == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif tokens[i] == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(tokens[i]))

        return stack.pop()

        
        