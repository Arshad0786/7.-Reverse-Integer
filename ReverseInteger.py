class Solution:
    def reverse(self, x=0):
        if(type(x) != type(int())):
            return None
        ReversedValue = 0
        isNegative = 0
        if(x < 0):
            isNegative = -1
            x = isNegative * x #to make x positive
        else:
            isNegative = 1
        length = len(str(x))
        for i in range(length):
            ReversedValue = ReversedValue + (x % 10) * (10 ** (length - (i+1)))
            x = x // 10
        if(ReversedValue > (2 ** 31)-1):
            return 0
        return ReversedValue * isNegative #if input is negative, it would be converted to positive number by timing -1 before all process,
                                          #so when outputing, we need to make it negative by timing it by -1 again.
