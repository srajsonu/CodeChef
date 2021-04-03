class Solution:
    def solve(self, A, n):
        cnt = 0
        for i in range(n-1):
            mn = min(A[i:n])
            j = A.index(mn)
            A[i:j+1] = A[i:j+1][::-1]
            cnt += (j - i + 1)

        return cnt


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = S.solve(A, N)
        print('Case #'+str(i+1)+':', ans)
