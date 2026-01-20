class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(50)]
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, 46):
            dp[i] = dp[i-1] + dp[i-2]
    
        return dp[n]
        
        