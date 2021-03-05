class Solution:
    def solve(self, T, N, H, x):
        for i in T:
            val = i + x
            if val >= H:
                return 'YES'

        return 'NO'


if __name__ == '__main__':
    S = Solution()
    N, H, x = map(int, input().split())
    T = list(map(int, input().split()))
    print(S.solve(T, N, H, x))
