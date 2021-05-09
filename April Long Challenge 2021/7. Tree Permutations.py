from collections import defaultdict


class Solution:
    def solve(self, A, B, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)





if __name__ == '__main__':
    P = Solution()
    T = int(input())
    for _ in range(T):
        N, S = map(int, input().split())
        edges = []
        for _ in range(N-1):
            u, v = map(int, input().split())
            edges.append([u, v])

        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        print(P.solve(A, B, edges))
