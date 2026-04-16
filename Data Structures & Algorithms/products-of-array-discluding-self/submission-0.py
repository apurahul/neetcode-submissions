class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)

        product = 1
        count_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                product *= nums[i]

        if count_zero > 1:
            return result

        for i, c in enumerate(nums):
            if count_zero:
                if c:
                    result[i] = 0
                else:
                    result[i] = product

            else:

                result[i] = product // nums[i]

        return result



