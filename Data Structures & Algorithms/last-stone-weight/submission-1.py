class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x > y:
                y = x - y
                heapq.heappush(stones, - y)
        stones.append(0)
        return - stones[0]
 

        
        