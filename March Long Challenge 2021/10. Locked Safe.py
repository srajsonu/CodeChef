class Solution:
    def solve(self, A, N):
        pair = []
        for i in range(N):
            for j in range(N):
                l = A[i]
                r = A[j]
                OR = l
                AND = l
                mx = l
                for k in range(l+1, r+1):
                    OR |= k
                    AND &= k
                    mx = max(mx, A[k])

                XOR = OR ^ AND
                if XOR >= mx:
                    pair.append([l, r])

        return pair



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(S.solve(A, N))
