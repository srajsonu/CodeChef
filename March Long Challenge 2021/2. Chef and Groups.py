class Solution:
    def solve(self, A):
        n = len(A)
        cnt = 0
        if A[0] == '1':
            cnt += 1

        for i in range(1, n):
            prev = A[i-1]
            curr = A[i]

            if prev == '0' and curr == '1':
                cnt += 1

        return cnt


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        A = input()
        print(S.solve(A))
