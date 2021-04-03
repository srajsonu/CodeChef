from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[i]):
            return False
        return True

    def solve(self, A, R, C):
        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]
        q = deque()
        q.append((0, 0))
        cnt = 0
        while q:
            i, j = q.popleft()
            tmp = A[i][j]
            A[i][j] = -1

            if tmp == -1:
                continue

            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                if self.isValid(A, nRow, nCol) and A[nRow][nCol] != -1:
                    val = 0

                    if tmp < A[nRow][nCol]:
                        val = A[nRow][nCol] - tmp - 1
                        tmp = val

                    if tmp > A[nRow][nCol]:
                        val = tmp - A[nRow][nCol] - 1
                        A[nRow][nCol] = val

                    cnt += val
                    q.append((nRow, nCol))

        return cnt



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for i in range(T):
        R, C = map(int, input().split())
        arr = []
        for _ in range(R):
            row = list(map(int, input().split()))
            arr.append(row)

        ans = S.solve(arr, R, C)
        print('Case #' + str(i + 1) + ':', ans)
