class Solution:
    def solve(self, A):
        pass

if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = []
        for _ in range(N):
            M = list(map(int, input().split()))
            arr.append(M)
        print(S.solve(arr))
