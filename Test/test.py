"""
1 : [2, 3]


7 <-> 6 (1)
6 <-> 5 (2)
2 <-> 8 (2)
0 <-> 1 (4)
2 <-> 5 (4)
6 <-> 8 (6)
2 <-> 3 (7)
7 <-> 8 (7)
3 <-> 4 (9)
5 <-> 4 (10)
1 <-> 7 (11)
3 <-> 5 (14)

 7 -> 6  -> 5 -> 4
            |
            2 -> 8

"""
from collections import defaultdict


class Solution:
    def find_root(self, A, parent):
        if parent[A] == A:
            return A
        return self.find_root(parent[A], parent)

    def union(self, A, B, height, parent):
        C = self.find_root(A, parent)
        D = self.find_root(B, parent)

        if C == D:
            return

        if height[C] < height[D]:
            parent[C] = D
        elif height[C] > height[D]:
            parent[D] = C
        else:
            parent[C] = D
            height[C] += 1

    def mst(self, A):
        graph = defaultdict(list)

        for i, j, k in A:
            graph[i].append([j, k])
            graph[j].append([i, k])

        graph = sorted(graph, key= lambda i: i[1])

        parent = []
        height = []


if __name__ == '__main__':
    A = [[0, 1, 4],
         [0, 7, 8],
         [1, 7, 11],
         [1, 2, 8],
         [2, 8, 2],
         [2, 5, 4],
         [3, 2, 7],
         [3, 5, 14]]


"""
class Solution:
    def dp(self, n, dp):
        if dp[n]:
            return dp[n]

        if n <= 1:
            return 1

        count = 0
        for i in range(1, n+1):
            count += self.dp(i-1, dp) * self.dp(n-i, dp)

        dp[n] = count
        return count


    def uniqueBST(self, A):
        dp = [0 for _ in range(A+1)]
        return self.dp(A, dp)

    def solve(self, n):
        dp = [0 for _ in range(n+1)]
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i - j]

        return dp[-1]


if __name__ == '__main__':
    A = 9
    B = Solution()
    print(B.uniqueBST(A))
    print(B.solve(A))

"""
class Solution:
    def solve(self, arr):
        m = len(arr)
        n = len(arr[0])

        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    for k in range(m):
                        if arr[k][j] == 0:
                            continue

                        arr[k][j] = -1

                    for l in range(n):
                        if arr[i][l] == 0:
                            continue
                        arr[i][l] = -1

        for i in range(m):
            for j in range(n):
                if arr[i][j] == -1:
                    arr[i][j] = 0

        # while q:
        #     i, j = q.pop(0) #(1, 1)
        #
        #     for k in range(n):
        #         arr[i][k] = 0
        #
        #     for k in range(m):
        #         arr[k][j] =  0
        return arr


if __name__ == '__main__':
    arr = [[1, 1, 1],
           [1, 0, 1],
           [1, 1, 1]]

    S = Solution()
    print(S.solve(arr))

"""
1 0 1
0 0 0
1 0 1

"""
