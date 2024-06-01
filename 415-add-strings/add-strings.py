class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        return str(int(num1) + int(num2))

        # n = int(num1) + int(num2)
        # jj = ""
        # while n:
        #     jj+= str(n%10)
        #     n = n//10
        # return jj