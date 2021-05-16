class Solution:
    def solve(self, n):
        mod = 10 ** 9 + 7
        cnt = n // 2 + 1

        return cnt % mod


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(S.solve(N))
