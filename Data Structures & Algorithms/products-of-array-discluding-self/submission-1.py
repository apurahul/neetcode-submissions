class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        #brute force apprach - just follo w the problem

        # n = len(nums)

        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):

        #         if j == i:
        #             continue

        #         prod *= nums[j]

        #     res[i] = prod

        # return res


        zero_count = 0

        prod = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num

        n = len(nums)

        res = [0] * n

        if zero_count > 1:
            return res
        
        for i in range(n):
            if zero_count == 1:
                if nums[i] == 0:
                    res[i] = prod
            else:
                res[i] = prod//nums[i]
            
        return res
            

        
        




        
        