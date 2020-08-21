#Leetcode 674 Longest Continous Substring
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        length = len(nums)
        dp = [1] * length
        for i in range(1,length):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)

#Leetcode 70 Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1] * n
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1] + arr[n-2]

#Leetcode 55 Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        maxIndex = 0
        for i in range(len(nums)):
            if maxIndex < i:
                return False
            maxIndex = max(maxIndex, i + nums[i])
            if maxIndex >= len(nums) -1:
                return True
        return maxIndex >= len(nums) -1

#Leetcode 1306 Jump Game 3
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr:
            return False
        length = len(arr)
        visited = set()
        if arr[start] == 0:
            return True
        queue = [start]
        
        while len(queue) != 0:
            current = queue.pop(0)
            left = current - arr[current]
            right = current + arr[current]
            if left >= 0 and left not in visited:
                if arr[left] == 0:
                    return True
                queue.append(left)
                visited.add(left)
            if right < length and right not in visited:
                if arr[right] == 0:
                    return True
                queue.append(right)
                visited.add(right)
        return False
#Leetcode 322 Coin Change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount +1) 
        dp[0] = 0
        for value in range(amount+1):                                  
            for coin in (coins):                                      
                if(coin <= value):                                
                    dp[value] = min(dp[value], 1 + dp[value - coin])                      
        if(dp[amount] == float("inf")):
            return -1
        else:
            return dp[amount]

# Leetcode 62 Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(n):
            grid.append([1]*m)
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]

# Leetcode 198 House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = nums[::]
        for i in range(length):
            for j in range(i-1):
                dp[i] = max(dp[j] + nums[i], dp[i])
        return max(dp)

# Leetcode 377 Combination Sum
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target +1)
        length = len(nums)
        dp[0] = 1
        for i in range(1,target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[target]

# Leetcode 121 Best time to buy and sell stock 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        length = len(prices)
        minimum = float("inf")
        for i in prices:
            if i < minimum:
                minimum = i
            profit = max(profit, i-minimum)
        return profit

# Leetcode Best time to buy and sell stock 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
        profit = 0
        for i in range(1,length):   
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

#Leetcode 139 Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length+1)
        dp[0] = True
        words = set(wordDict)
        for i in range(1, length+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
        return dp[length]