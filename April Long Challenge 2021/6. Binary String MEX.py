class Solution:
    def build(self, A, key):
        key = bin(key).replace('0b', '')
        m = len(A)
        n = len(key)
        i = 0
        j = 0

        while i < m and j < n:
            if A[i] == key[j]:
                i += 1
                j += 1
            else:
                i += 1

        return True if j == n else False

    def solve(self, A):
        freq = {}
        for i in A:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        i = 0

        while i < int(A, 2):
            ans = self.build(A, i)
            if not ans:
                return bin(i).replace('0b', '')

            i += 1

        return 0

        # while l <= h:
        #     mid = (l + h) // 2
        #     if self.build(A, mid):
        #         l = mid + 1
        #     else:
        #         h = mid - 1
        #
        # return l


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        A = input()
        print(S.solve(A))
