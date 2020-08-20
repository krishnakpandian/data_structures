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