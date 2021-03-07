class Solution:
    def solve(self, N, E, H, A, B, C):
        egg = E
        bar = H
        people = N
        prices = {
            "omelette": A,
            "milk_shake": B,
            "cake": C
        }
        prices = sorted(prices.items(), key=lambda i: i[1])

        while egg and bar and people > 0:
            no_of_omelette = 0
            no_of_shake = 0
            no_of_cake = 0
            for dish, price in prices:
                if dish == "omelette":
                    no_of_omelette = egg // 2
                    egg -= no_of_omelette * 2
                    people -= no_of_omelette

                    #TODO: Take care of people
                    if people < 0:
                        return N * price

                    #TODO: Take care of Incredients

                    if people == 0:
                        return no_of_omelette * price

                if dish == "milk_shake":
                    no_of_shake = bar // 3
                    bar -= no_of_shake * 3
                    people -= no_of_shake

                    #TODO: Take care of people

                    # TODO: Take care of Incredients

                    if people == 0:
                        return no_of_omelette * A + no_of_shake * price


                if dish == "cake":
                    no_of_cake = min(bar, egg)
                    egg -= no_of_cake
                    bar -= no_of_cake
                    people -= no_of_cake

                    #TODO: Take care of people

                    # TODO: Take care of Incredients

                    if people == 0:
                        return no_of_omelette * A + no_of_shake * B + no_of_cake * price

            if people == 0:
                return no_of_omelette + no_of_shake + no_of_cake

            print(no_of_omelette, no_of_shake, no_of_cake, people)
            break





if __name__ == '__main__':
    S = Solution()
    T = 1
    for _ in range(T):
        N, E, H, A, B, C = 4, 5, 5, 1, 2, 3
        print(S.solve(N, E, H, A, B, C))
