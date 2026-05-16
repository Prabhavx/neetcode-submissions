class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []
        le = 0
        ops = ['+', '-', '*', '/']

        for exp in tokens:
            stk.append(exp)
            if exp in ops:
                opr = stk.pop()
                num2 = int(stk.pop()); num1 = int(stk.pop())

                match opr:
                    case '+': stk.append(num1+num2)
                    case '-': stk.append(num1-num2)
                    case '*': stk.append(num1*num2)
                    case '/': stk.append(int(num1/num2))

        return int(stk[-1])

                


        