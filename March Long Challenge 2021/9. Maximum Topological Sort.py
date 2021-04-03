from collections import defaultdict


class Solution:
    def solve(self, A, N, K):
        graph = defaultdict(list)

        inDegree = [0 for _ in range(N)]
        for i, j in A:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)


        # for i in graph:
        #     for j in graph[i]:
        #         inDegree[j] += 1

        return graph, inDegree


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = []
        for _ in range(N-1):
            u, v = map(int, input().split())
            A.append([u, v])

        print(S.solve(A, N, K))
