class Solution:
    def solve(self, k1, k2, k3, v):
        d = 100
        t = 9.58
        total_speed = k1 * k2 * k3 * v
        total_time = d / total_speed
        total_time = round(total_time, 2)

        if total_time < t:
            return 'YES'
        else:
            return 'NO'



if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        k1, k2, k3, v = map(float, input().split())
        print(S.solve(k1, k2, k3, v))
