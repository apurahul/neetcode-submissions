class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # num_to_index = {}

        # for i, num in enumerate(numbers):
        #     comp = target - num

        #     if comp in num_to_index:
        #         return [num_to_index[comp], i + 1]
                
        #     num_to_index[num] = i + 1
        
        # return []
        
        # the above approach uses  a hashmap and because the array is  ascending, ther open already present in the list is the smaller index

        # below is moreoptimal 2 pointer approach for bretter space

        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
                
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []



                

        