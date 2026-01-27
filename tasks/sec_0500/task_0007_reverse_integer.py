class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        num = abs(x)

        result = 0
        while num > 0:
            digit = num % 10
            num //= 10

            if result > (2**31 - 1 - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result