class Solution:
    def dp(self, A, i, req, res, dp):
        global ans
        if req <= 0:
            self.res = res
            return 0

        if dp[i][req]: return dp[i][req]

        if i == len(A):
            ans = float('inf')
        else:
            take = self.dp(A, i + 1, req - A[i], res + [A[i]], dp) + 1
            dont = self.dp(A, i + 1, req, res, dp)
            ans = min(take, dont)

        dp[i][req] = ans
        return ans

    def solve(self, N, K, H):
        if not H or not K: return -1
        self.res = []
        res = 0
        for _ in range(2):
            dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
            tmp = self.res
            H = [i for i in H if not i in tmp or tmp.remove(i)]
            ans = self.dp(H, 0, K, [], dp)
            if ans == float('inf'): return -1
            res += ans

        return res if res != float('inf') else -1


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        H = list(map(int, input().split()))
        print(S.solve(N, K, H))
