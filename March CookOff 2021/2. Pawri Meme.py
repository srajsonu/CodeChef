class Solution:
    def solve(self, A):
        return A.replace('party', 'pawri')


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        A = input()
        print(S.solve(A))
