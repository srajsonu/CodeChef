class Solution:
    def solve(self, N, E, H, A, B, C):
        ans = []
        egg = E
        bar = H
        people = N
        while egg and bar:
            global omelette, milk_shake, cake
            if A < B and A < C:
                omelette = E // 2
                egg -= omelette * 2
                people -= omelette

            if B > A and B < C:
                milk_shake = H // 3
                bar -= milk_shake * 3
                people -= milk_shake

            if C > A and C > B:
                cake = min(egg, bar)
                people -= cake

            if people == 0:
                total_price = omelette * A + milk_shake * B + cake * C
                return total_price

            break



if __name__ == '__main__':
    S = Solution()
    T = 1
    for _ in range(T):
        N, E, H, A, B, C = 4, 5, 5, 1, 2, 3
        print(S.solve(N, E, H, A, B, C))
