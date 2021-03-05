class Solution:
    def solve(self, A):
        n = len(A)



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, M, X, Y = map(int, input().split())
        arr = []
        for _ in range(M):
            A, B, C, D = map(int, input().split())
            arr.append([A, B, C, D])
        print(S.solve(arr))
