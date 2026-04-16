class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #brutw force:

        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))
        
        # return list(res)

        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i -1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:

                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1

                    while l < r and nums[l] == nums[l - 1]:
                        l +=1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res







        