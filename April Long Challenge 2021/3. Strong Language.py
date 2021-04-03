class Solution:
    def solve(self, A, n, k):
        cnt = 0
        ans = 0
        for i in range(n):
            if A[i] == '*':
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
            ans = max(ans, cnt)

        if ans >= k:
            return 'YES'
        else:
            return 'NO'



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = input()
        print(S.solve(A, N, K))
