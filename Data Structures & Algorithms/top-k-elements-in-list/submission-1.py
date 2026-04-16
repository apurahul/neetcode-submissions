class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach using hash maps and sorting

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)


        arr =[]
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()

        res =[]



        while len(res) < k:
            res.append(arr.pop()[1])

        return res


