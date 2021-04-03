class Solution:
    def solve(self, A):
        pass


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for i in range(T):
        R, C = map(int, input().split())
        arr = []
        for _ in range(R):
            row = list(map(int, input().split()))
            arr.append(row)

        ans = S.solve(arr)
