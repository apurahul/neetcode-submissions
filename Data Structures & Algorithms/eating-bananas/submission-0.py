class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the speed can range from 1 to the max of the pile

        l, r = 1, max(piles) # max(piles) give the speed at which koko can eat all the bananas of that pile within an hour
        # so iterating over an imaginalry speed pile from 1 to max(piles)

        # this is a monotic function type of problem, where we have to find the minimum
        while l < r:
            speed = l + ((r - l)// 2)

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / speed)
            
            if totalTime <= h:
                r = speed
            else:
                l = speed + 1
        
        return l

        