from itertools import permutations

class Solution:
    def solve(self, N, C):
        A = [i for i in range(1, N+1)]
        flag = 0

        for i in permutations(A):
            B = list(i)
            cnt = 0
            for j in range(N-1):
                mn = min(B[j:N])
                k = B.index(mn)
                B[j:k+1] = B[j:k+1][::-1]
                cnt += (k-j+1)

            if cnt == C:
                flag = 1
                return B, flag

        return "IMPOSSIBLE", flag


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, C = map(int, input().split())
        ans, flag = S.solve(N, C)
        if flag == 1:
            ans = [str(i) for i in ans]
            ans = " ".join(ans)
            print('Case #' + str(_ + 1) + ':', ans, sep=" ")
        else:
            print('Case #' + str(_ + 1) + ':', ans)
