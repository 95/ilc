# Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    @staticmethod
    def check_range(value):
        if value < -2**31 or value > 2**31 - 1:
            return 0
        else:
            return value
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        reversed_value = int(str(x)[::-1]) * sign
        return Solution.check_range(reversed_value)

if __name__ == '__main__':
    soln = Solution()
    print(soln.reverse(-6665))
