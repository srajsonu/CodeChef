from heapq import *
class Solution:
    def solve(self, A, B):
        if not A or not B: return -1
        v1 = sum(A)
        v2 = sum(B)
        if v1 > v2: return 0
        B = [-i for i in B]
        heapify(A)
        heapify(B)
        cnt = 0
        while v1 <= v2:
            tmp1 = heappop(A) if A else float('inf')
            tmp2 = -heappop(B) if B else float('-inf')
            if tmp1 >= tmp2:
                return -1
            elif tmp1 < tmp2:
                v1 = (v1 - tmp1) + tmp2
                v2 = (v2 - tmp2) + tmp1

            cnt += 1

        return cnt

if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(S.solve(A, B))
