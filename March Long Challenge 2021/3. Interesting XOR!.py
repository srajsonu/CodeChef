class Solution:
    def solve(self, A):
        ans = 0
        d = 1
        while 2 ** d < A:
            d += 1

        h = 2 ** d
        for i in range(1, h):
            tmp = i ^ A
            print(i, tmp)
            ans = max(ans, i * tmp)

        return ans


if __name__ == '__main__':
    S = Solution()
    T = 1
    for _ in range(T):
        C = 13
        print(S.solve(C))
