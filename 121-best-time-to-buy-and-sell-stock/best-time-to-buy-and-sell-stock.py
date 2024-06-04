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


        j = 0
        jj = prices[0]
        for p in prices[1:]:
            if p>jj:
                j = max(j, p-jj)
            else: jj = p

        return j
        