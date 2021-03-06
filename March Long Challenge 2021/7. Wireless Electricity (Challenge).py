class Solution:
    def solve(self, A, B):
        pass


if __name__ == '__main__':
    S = Solution()
    N, M = map(int, input().split())
    arr1 = []
    for _ in range(N):
        X, Y = map(int, input().split())
        arr1.append([X, Y])
    arr2 = []
    for _ in range(M):
        A, B, C, D = map(int, input().split())
        arr2.append([A, B, C, D])

    print(S.solve(arr1, arr2))
