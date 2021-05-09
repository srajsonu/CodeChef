class Solution:
    def solve(self, A, B, n, m, e):
        pass


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, M, E = map(int, input().split())
        A = []
        for _ in range(N):
            i = input()
            A.append(i)

        B = []
        for _ in range(N):
            i = input()
            B.append(i)

        print(S.solve(A, B, N, M, E))
