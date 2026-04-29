class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # triplets = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplets.add(tuple(sorted(
        #                     [nums[i], nums[j], nums[k]])))
                    
        # return [list(i) for i in triplets]

        #2 pointer approach
        nums.sort()
        triplets = []

        

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if  i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l -1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1

        
        return triplets

        