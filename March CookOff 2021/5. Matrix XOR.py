class Solution:
    def solve(self, N, M, K):
        xor = 0
        if N == M:
            for i in range(1, N+1):
                xor ^= (K + i + i)

        elif N < M:
            for i in range(1, N+1):
                xor ^= (K + i + i)

            for i in range(1, N+1):
                for j in range(N+1, M+1):
                    xor ^= (K + i + j)

        else:
            for i in range(1, M+1):
                xor ^= (K + i + i)

            for i in range(M+1, N+1):
                for j in range(M):
                    xor ^= (K + i + j)

        return xor


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        print(S.solve(N, M, K))
