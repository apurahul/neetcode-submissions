class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        value_to_index = {}

        for i, num in enumerate(nums):
            contemp = target - num

            if contemp in value_to_index:
                return [value_to_index[contemp], i]
            else:
                value_to_index[num] = i
        