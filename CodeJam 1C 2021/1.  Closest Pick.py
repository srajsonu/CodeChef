class Solution:
    def solve(self, N, K, P):
        if not K or not P:
            return 0

        if N < 2:
            return ((P[0] - 1) + (K - P[0])) / K

        P.sort()
        diff = []
        for i in range(1, N):
            tmp = P[i] - P[i - 1]
            diff.append(tmp)

        last = K - P[-1]
        diff.append(last)
        diff.sort()

        mx1 = diff[-1] - 1 if diff[-1] != 0 else diff[-1]
        mx2 = diff[-2] - 1 if diff[-2] != 0 else diff[-2]

        return (mx1 + mx2) / K


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        P = list(map(int, input().split()))
        ans = S.solve(N, K, P)
        print('Case #' + str(_ + 1) + ':', ans)
