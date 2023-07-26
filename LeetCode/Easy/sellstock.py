class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(currentProfit, profit)
            else:
                left = right
            right += 1
        return profit