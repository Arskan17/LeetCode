class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # jj = []

        # if all([prices[i]>=prices[i+1] for i in range(n-1)]): return 0

        # for i in range(n-1):
        #     tmp = max(prices[i+1:n]) - prices[i]
        #     jj.append(tmp)



        # n = len(prices)
        # jj = [(max(prices[i+1:n]) - prices[i]) for i in range(n-1)]

        # if max(jj)<1: return 0
        # return max(jj)


        profit = 0
        lastBoughtAt = prices[0]

        for currentPrice in prices[1:]:
            if currentPrice > lastBoughtAt:
                profit = max(profit, (currentPrice - lastBoughtAt))
            else:
                lastBoughtAt = currentPrice

        return profit
        