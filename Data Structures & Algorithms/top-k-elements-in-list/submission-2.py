class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach using hash maps and sorting

        # count = {}

        # for i in range(len(nums)):
        #     count[nums[i]] = 1 + count.get(nums[i], 0)


        # arr =[]
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        
        # arr.sort()

        # res =[]



        # while len(res) < k:
        #     res.append(arr.pop()[1])

        # return res


        #heap sort

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        heap = []

    
        for i, freq in count.items():
            heapq.heappush(heap, [freq, i])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res    


