class Solution:
    def solve(self, A, N, K):
        cnt = 0
        for i in range(1, N//2+1):
            if A[i-1] != A[N-i]:
                cnt += 1


        return abs(cnt-K)


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        A = input()
        ans = S.solve(A, N, K)
        print('Case #'+str(i+1)+':', ans)
