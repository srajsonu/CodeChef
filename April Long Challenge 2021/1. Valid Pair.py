class Solution:
    def solve(self, A, B, C):
        if A == B or B == C or A == C:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    A, B, C = map(int,input().split())
    S = Solution()
    print(S.solve(A, B, C))
