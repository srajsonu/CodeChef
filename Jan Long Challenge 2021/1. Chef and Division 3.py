class Solution:
    def solve(self, N, K, D, A):
        if not A or not K: return 0
        req_que = K * D
        que = sum(A)
        if req_que <= que:
            return D

        return que // K

if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, K, D = map(int, input().split())
        A = list(map(int, input().split()))
        print(S.solve(N, K, D, A))
