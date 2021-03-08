from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def dfs(self, A, B, i, j, vis):
        vis.add(i, j)

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis:
                self.dfs(A, B, nRow, nCol, vis)


    def bfs(self, A, B, X, i, j, vis):
        q = deque()
        q.append((i, j, B[i][j] - A[i][j]))
        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        while q:
            i, j, v = q.popleft()
            A[i][j] += v

            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if self.isValid(A, nRow, nCol) and A[nRow][nCol] != B[nRow][nCol]:
                    while self.isValid(A, nRow, nCol):
                        A[nRow][nCol] += v
                        nRow += r
                        nCol += c

                    X -= 1

                # print(nRow-r, nCol-c, A)
                if self.isValid(A, nRow - r, nCol - c) and A[nRow - r][nCol - c] != B[nRow - r][nCol - c] and (
                nRow - r, nCol - c) not in vis and X > 0:

                    #print(nRow - r, nCol - c, A, v)
                    vis.add((nRow - r, nCol - c))
                    v = B[nRow - r][nCol - c] - A[nRow - r][nCol - c]
                    q.append((nRow - r, nCol - c, v))

            if X <= 0:
                break


    def solve(self, A, B, R, C, X):
        vis = set()
        for i in range(R):
            for j in range(C):
                if A[i][j] != B[i][j] and (i, j) not in vis:
                    self.bfs(A, B, X, i, j, vis)

        for i in range(R):
            for j in range(C):
                if A[i][j] != B[i][j]:
                    return 'No'

        return A


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        R, C, X = map(int, input().split())

        A = []
        for _ in range(R):
            row = list(map(int, input().split()))
            A.append(row)

        B = []
        for _ in range(R):
            row = list(map(int, input().split()))
            B.append(row)

        print(S.solve(A, B, R, C, X))
