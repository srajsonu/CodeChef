class Solution:
    def solve(self, w1, w2, x1, x2, M):
        gain_wt = w2 - w1
        max_inc = x2 * M
        min_inc = x1 * M

        if max_inc >= gain_wt and min_inc <= gain_wt:
            return 1
        return 0


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        w1, w2, x1, x2, M = map(int, input().split())
        print(S.solve(w1, w2, x1, x2, M))
