class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        curr_profit = 0
        max_profit = 0
        for i in prices:
            if i<buy_price: buy_price = i
            curr_profit = i - buy_price
            max_profit = max(max_profit,curr_profit)
        return max_profit if max_profit>0 else 0