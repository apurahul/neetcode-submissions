class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # brute force way - repeated check the array for operaorda dn solve the first 2 elemsts before it

        # while len(tokens) > 1:
        #     for i in range(len(tokens)):

        #         if tokens[i] in "+-*/":
        #             a = int(tokens[i-2])
        #             b = int(tokens[i-1])

        #             if tokens[i] == "+":
        #                 resullt = a + b
        #             elif tokens[i] == "-":
        #                 resullt = a - b
        #             elif tokens[i] == "*":
        #                 resullt = a * b
        #             elif tokens[i] == "/":
        #                 resullt = int(a / b)
        #             tokens = tokens[:i - 2] + [str(resullt)] + tokens[i + 1:]

        #             break
        # return int(tokens[0])



        ##stack method

        stack = []

        for i in range(len(tokens)):

            if tokens[i] in '+-*/':
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == "+":
                    result = b + a
                elif tokens[i] == "-":
                    result = b - a
                elif tokens[i] == "*":
                    result = a * b
                elif tokens[i] == "/":
                    result = int(b / a)
            
                stack.append(result)

            
            else:
                stack.append(int(tokens[i]))

        return stack[0]
                    
        