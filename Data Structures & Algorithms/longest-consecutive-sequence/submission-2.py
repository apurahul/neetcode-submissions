class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # nums.sort()

        # max_length = 1
        # length = 0
        # curr = nums[0]
        # i = 0
        # while i < len(nums):
        #     if nums[i] != curr:
        #             curr = nums[i]
        #             length = 0
        #     while i < len(nums) and nums[i] == curr:
        #         i +=1
        #     curr += 1
        #     length += 1
        #     max_length = max(max_length, length)

        # return max_length


        #optimal

        if not nums:
            return 0
        
        numset = set(nums)

        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                length = 1

                while (num + length) in numset:
                    length += 1

                longest = max(longest, length)

        return longest
            




        