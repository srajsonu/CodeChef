class Solution:
    def solve(self, X, A, B):
        req = A + (100 - X) * B
        return req * 10


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        X, A, B = map(int, input().split())
        print(S.solve(X, A, B))
