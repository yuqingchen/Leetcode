class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) - 1 
        neg = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor :
            temp, i = divisor, 1 
            while dividend >= temp :
                dividend -= temp
                res += i
                i <<= 1 
                temp <<= 1 
        if neg :
            res = - res
        if res < -INT_MAX - 1 :
            return -INT_MAX - 1 
        if res > INT_MAX :
            return INT_MAX 
        return res
        