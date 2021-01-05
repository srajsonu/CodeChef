class Solution:
    def solve(self, n, s):
        if not n: return ''
        ans = ''
        for i in range(0, n-1, 4):
            tmp = s[i:i+4]
            char = int(tmp, 2)
            ans += chr(97 + char)

        return ans

if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input()
        print(S.solve(n, s))
