class Solution:
    def solve(self, A):
        tmp = 10 ** 6
        if not A or A >= tmp:
            return -1
        if A % 2 == 0 and A % 10 == 0:
            return 1
        else:
            return 0


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        A = int(input())
        print(S.solve(A))
