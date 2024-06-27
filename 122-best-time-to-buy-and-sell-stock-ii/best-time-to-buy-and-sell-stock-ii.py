class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lastBoughtAt = prices[0]

        for currentPrice in prices[1:]:
            if currentPrice > lastBoughtAt:
                profit += currentPrice - lastBoughtAt

            lastBoughtAt = currentPrice
        return profit
        