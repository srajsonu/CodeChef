from collections import deque


class Solution:
    def isValid(self, A, i):
        if i < 0 or i >= len(A):
            return False
        return True

    def Solve(self, X, Y, A):
        n = len(A)
        A = [i for i in A]
        q = deque()
        for i in A:
            if i == '?':
                q.append(i)
        vis = set()
        while q:
            i = q.popleft()
            if i > 0 and i < n and A[i-1] == '?' and A[i] == '?' and A[i+1] == '?':
                q.append(i-1)
                q.append(i+1)

            if i == 0:
                if A[i + 1] == 'C':
                    A[i] = 'C'
                    vis.add(i)
                elif A[i+1] == 'J':
                    A[i] = 'J'
                    vis.add(i)
                else:
                    q.append(i+1)

            if i == n-1:
                A[i] = A[i-1]
                if A[i-1] == 'C':
                    A[i] = 'C'
                    vis.add(i)
                elif A[i-1] == 'J':
                    A[i] = 'J'
                    vis.add(i)
                else:
                    q.append(i-1)

        return A


    def solve(self, X, Y, A):
        X = int(X)
        Y = int(Y)
        A = [i for i in A]
        n = len(A)
        sizeC = 0
        sizeJ = 0
        for i in A:
            if i == 'C':
                sizeC += 1
            elif i == 'J':
                sizeJ += 1

        if not sizeC or not sizeJ:
            return 0

        for i in range(1, n - 1):
            if A[i - 1] == '?' and A[i] == 'C' and A[i + 1] == '?':
                A[i - 1] = 'C'
                A[i + 1] = 'C'

            if A[i - 1] == '?' and A[i] == 'J' and A[i + 1] == '?':
                A[i - 1] = 'J'
                A[i + 1] = 'J'

            if A[i - 1] == 'C' and A[i] == '?' and A[i + 1] == 'J':
                if X < Y:
                    A[i - 1] = 'J'
                    A[i + 1] = 'J'
                elif X > Y:
                    A[i - 1] = 'C'
                    A[i + 1] = 'C'

            if A[i - 1] == 'J' and A[i] == '?' and A[i + 1] == 'C':
                if X < Y:
                    A[i - 1] = 'J'
                    A[i + 1] = 'J'
                elif X > Y:
                    A[i - 1] = 'C'
                    A[i + 1] = 'C'

        cnt = 0
        print(A)
        for i in range(1, n):
            if A[i-1] == 'C' and A[i] == 'J':
                cnt += X

            if A[i-1] == 'J' and A[i] == 'C':
                cnt += Y

        return cnt


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for i in range(T):
        X, Y, A = map(str, input().split())
        ans = S.Solve(X, Y, A)
        print('Case #' + str(i + 1) + ':', ans)


"""
x = 2
y = -5

STR = JCJCJCJCJC -> JCCJCCJCJC


2 5 ??J???
"""
