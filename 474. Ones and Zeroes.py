class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def countPair(s):
            m, n = 0, 0
            for c in s:
                if c == '0':
                    m += 1
                else:
                    n += 1
            return m, n

        prevDp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        # dp = [[[0 for _ in xrange(n+1)] for _ in xrange(m+1)] for _ in xrange(len(strs) + 1)]

        for i in xrange(1, len(strs) + 1):
            dp, prevDp = prevDp, dp
            mNeed, nNeed = countPair(strs[i-1])
            for M in xrange(m + 1):
                for N in xrange(n + 1):
                    # print mNeed, nNeed, M, N
                    if mNeed <= M and nNeed <= N:
                        dp[M][N] = max(prevDp[M-mNeed][N-nNeed] + 1, prevDp[M][N])
                        # dp[i][M][N] = max(dp[i-1][M-mNeed][N-nNeed] + 1, dp[i-1][M][N])
                    else:
                        dp[M][N] = prevDp[M][N]
                        # dp[i][M][N] = dp[i-1][M][N]

        return dp[m][n]
        # return dp[len(strs)][m][n]

        # def dfs(strPairs, m, n, i, memo):
        #     if i == len(strPairs):
        #         return 0

        #     key = (m, n, i)
        #     if key not in memo:

        #         M, N = strPairs[i]

        #         if M <= m and N <= n:
        #             memo[key] = max(dfs(strPairs, m, n, i+1, memo), dfs(strPairs, m-M, n-N, i+1, memo) + 1)
        #         else:
        #             memo[key] = dfs(strPairs, m, n, i+1, memo)
        #         print 'atlas'

        #     print 'tinker'

        #     return memo[key]


        # return dfs(strPairs, m, n, 0, {})

        # def dfs(strPairs, m, n, memo):
        #     key = tuple(strPairs)
        #     if key not in memo:
        #         memo[key] = 0
        #         for i in xrange(len(strPairs)):
        #             mUsed, nUsed = strPairs[i]
        #             if mUsed <= m and nUsed <= n:
        #                 memo[key] = max(memo[key], dfs(strPairs[:i] + strPairs[i+1:], m - mUsed, n - nUsed, memo))

        #     return memo[key] + 1

        # return dfs(strPairs, m, n, {}) - 1
