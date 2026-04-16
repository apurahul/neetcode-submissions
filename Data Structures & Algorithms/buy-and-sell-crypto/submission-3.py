class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0

        #brute force way:

        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] < prices[i]:
        #             continue
        #         else:
        #             profit = prices[j] - prices[i]

        #         maxprofit = max(profit, maxprofit)
        
        # return maxprofit


        # 2 pointer approach

        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                r +=  1
                maxprofit = max(maxprofit, profit)
        
        return maxprofit







        

