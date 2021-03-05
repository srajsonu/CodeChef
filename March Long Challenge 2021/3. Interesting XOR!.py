class Solution:
    def solve(self, A):
        ans = []
        for i in range(A):
            for j in range(i+1, A):
                if i ^ j == A:
                    ans.append((i, j))

        return ans



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        C = 13
        print(S.solve(C))
