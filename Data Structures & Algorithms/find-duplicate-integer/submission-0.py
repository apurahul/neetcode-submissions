class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # seen = set()

        # for i in nums:
        #     if i in seen:
        #         return i
            
        #     seen.add(i)

        # return -1
        
        # a little confuing but constant space operation

        for num in nums:
            idx = abs(num) - 1 

            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1

        return -1       