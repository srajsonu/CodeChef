class Solution:
    def solve(self, A, B, C): # ans = A, need = B, no_of_que = C
        n = len(A)
        ans = [0 for _ in range(n)]

        for i, (j, k) in enumerate(zip(A, B)):
            ans[i] = k - j

        for i in range(1, n):
            ans[i] += ans[i-1]

        ans.sort()

        cnt = 0
        for i in range(n):
            if ans[i] <= C:
                cnt += 1

        return cnt


if __name__ == '__main__':
    A = [24, 27, 0]
    B = [51, 52, 100]
    C = 200
    D = Solution()
    print(D.solve(A, B, C))
