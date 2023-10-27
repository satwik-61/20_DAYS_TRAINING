class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1



    
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[amount + 1] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
        return dp[len(coins)][amount] if dp[len(coins)][amount] <= amount else -1

"""



