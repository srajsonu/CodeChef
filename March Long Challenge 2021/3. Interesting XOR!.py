class Solution:
    def solve(self, C):
        A = "1"
        B = "0"
        C = bin(C).replace('0b', '')
        for i in range(1, len(C)):
            if C[i] == '0':
                A += '1'
                B += '1'
            else:
                A += '0'
                B += '1'

        return int(A, 2) * int(B, 2)


if __name__ == '__main__':
    S = Solution()
    T = 1
    for _ in range(T):
        C = 13
        print(S.solve(C))
