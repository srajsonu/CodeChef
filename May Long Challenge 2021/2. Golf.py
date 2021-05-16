class Solution:
    def solve(self, N, x, k):
        l = 0
        h = N+1

        #Forward
        while l <= h:
            mid = (l + h) // 2
            if mid * k == x:
                return 'YES'
            elif mid * k < x:
                l = mid + 1
            else:
                h = mid - 1

        #Backward
        l = N+1
        h = 0

        while h <= l:
            mid = (l + h) // 2
            if (N+1 - mid*k) == x:
                return 'YES'
            elif (N+1 - mid*k) < x:
                l = mid - 1
            else:
                h = mid + 1

        return 'NO'


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N, x, k = map(int, input().split())
        print(S.solve(N, x, k))
