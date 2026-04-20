class Solution:
    def findMin(self, nums: List[int]) -> int:
        # monotonic function - binary search can be used

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
    
        return nums[l]
        