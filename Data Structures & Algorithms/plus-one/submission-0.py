class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        
        # integer = "".join(str(i) for i in digits)
        
        # integer1 = int(integer)

        # integer2 = integer1 + 1

        # final = list(str(integer2))

        # final = [int(x) for x in final]

        # return final

        n = len(digits)

        for i in range(n -1, -1 , -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
        