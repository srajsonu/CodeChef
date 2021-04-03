class Solution:
    def solve(self, n):
        if not n: return 0
        if n == 1: return 20
        if n == 2: return 34

        total_stack = n // 2
        total_sum = 34

        ans = total_sum * total_stack
        if n % 2 == 0:
            return ans
        else:
            return ans + 20



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(S.solve(N))
