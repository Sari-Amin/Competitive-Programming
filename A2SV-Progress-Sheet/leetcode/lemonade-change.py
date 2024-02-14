class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numberoffive = 0
        numbersoften = 0
        for c in bills:
            print(numberoffive, numbersoften)
            if c == 5:
                numberoffive += 1
            elif c == 10:
                if numberoffive >= 1:
                    numberoffive -= 1
                else:
                    return False
                numbersoften += 1
            else:
                if numbersoften >= 1 and numberoffive >= 1:
                    numbersoften -= 1
                    numberoffive -= 1
                elif numberoffive >= 3:
                    numberoffive -= 3
                else:
                    return False
        return True