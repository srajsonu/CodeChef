import sys

class Solution:
    def dp(self, A, idx, prev, dp):
        if idx == len(A):
            return 0

        # key = str(idx) + str(prev)
        # if key in dp:
        #     return dp[key]

        pick = 0
        if A[idx] > prev:
            pick = 1 + self.dp(A, idx + 1, A[idx], dp)

        dont = self.dp(A, idx+1, prev, dp)
        return max(pick, dont)
        # dp[key] = max(pick, dont)
        # return dp[key]

    def lengthOfLIS(self, nums):
        dp = {}
        return self.dp(nums, 0, float('-inf'), dp)

    def solve(self, A):
        n = len(A)

        ans = 1
        dp = [1 for _ in range(n)]

        prev = float('-inf')
        for i in range(n):
            cnt = 0
            if A[i] > prev:
                dp[i] += 1
                prev = A[i]

            for j in range(i + 1, n - 1):
                if A[j] > prev:
                    cnt += 1
                    prev = A[j]


            ans = max(ans, cnt)

        return ans

'''
A = [10,9,2,5,3,7,101,18]
^
cnt = 2
prev = 10, 101
i = 0 -> prev = -inf, curr = A[i] ---> curr > prev -- > cnt = 1,

j = 1
prev = -inf
take = 0
if A[i] > prev:
    take = 1 + self.dp(A, i+1, A[i])

dont = self.dp(A, i+1, prev)
return max(take, dont)

'''



if __name__ == '__main__':
    A = [10,9,2,5,3,7,101,18]
    B = Solution()
    print(B.solve(A))

