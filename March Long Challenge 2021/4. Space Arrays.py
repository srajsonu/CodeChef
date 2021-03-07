class Solution:
    def solve(self, A, n):
        if not n:
            return 'First'

        cnt = 0
        for i in range(n):
            if A[i] < i+1:
                cnt += ((i + 1) - A[i])


        if cnt % 2 != 0:
            return 'First'
        else:
            return 'Second'


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(S.solve(A, N))
