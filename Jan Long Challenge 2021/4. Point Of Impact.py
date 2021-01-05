class Solution:
    def solve(self, n, k, x, y):
        i = x
        j = y
        if not n or not k or x < 0 or y < 0: return (0, 0)
        if i == j and k <= 0:
            return (i, j)
        if i == j and k > 0:
            return (n, n)
        ans = []
        dir = 0
        cnt = 0
        while cnt < 4:
            if dir == 0:
                idx = max(i, j)
                i += (n - idx)
                j += (n - idx)
                dir = 1
            elif dir == 1:
                idx = min(i, j)
                i -= (n - idx)
                j += (n - idx)
                dir = 2
            elif dir == 2:
                idx = min(i, j)
                i -= (n - idx)
                j -= (n - idx)
                dir = 3
            else:
                idx = max(i, j)
                i += (n - idx)
                j -= (n - idx)
                dir = 0
            ans.append((i, j))
            cnt += 1

        if k <= 4:
            return ans[k - 1]
        return ans[(k % 4) - 1]


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, K, x, y = map(int, input().split())
        print(S.solve(N, K, x, y))
