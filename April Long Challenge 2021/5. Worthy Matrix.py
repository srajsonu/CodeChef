import copy

class Solution:
    def solve(self, arr, n, m, K):
        l = 0
        h = min(n, m) / 2
        A = copy.deepcopy(arr)

        for i in range(n):
            for j in range(1, m):
                A[i][j] += A[i][j-1]

        for i in range(1, n):
            for j in range(m):
                A[i][j] += A[i-1][j]

        cnt = 0
        for i in range(l, h):
            for j in range(n-i):
                for k in range(m-i):
                    total_size = (i+1) * (i+1)
                    total_sum = 0
                    avg = 0
                    if i == 0:
                        total_sum = arr[j][k]
                        avg = total_sum
                    else:
                        if j == 0 and k == 0:
                            total_sum = A[j+i][k+i]
                        elif j == 0:
                            total_sum = A[j+i][k+i] - A[j+i][k-1]

                        elif k == 0:
                            total_sum = A[j+i][k+i] - A[j-1][k+i]

                        else:
                            total_sum = A[j + i][k + i] - A[j-1][k+i] - A[j+i][k-1] + A[j-1][k-1]

                        avg = total_sum / total_size

                    if avg >= K:
                        cnt += 1

        return cnt

if __name__ == '__main__':
    S = Solution()
    B = [[2, 2, 3],
         [3, 4, 5],
         [4, 5, 5]]
    print(S.solve(B, 3, 3, 4))


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        B = []
        for _ in range(N):
            tmp = list(map(int, input().split()))
            B.append(tmp)

        print(S.solve(B, N, M, K))
