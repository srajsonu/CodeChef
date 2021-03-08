class Solution:
    def solve(self, A):
        freq = {}
        ans = []

        for i in A:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in A:
            freq[i] -= 1
            if freq[i] == 0:
                ans.append(i)

        return ans


if __name__ == '__main__':
    S = Solution()
    N = int(input())
    A = list(map(int, input().split()))
    print(S.solve(A))
