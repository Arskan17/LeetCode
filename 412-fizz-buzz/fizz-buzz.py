class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        jj = []
        for i in range(1, n+1):
            if (i%3 == 0) and (i%5 == 0): jj.append("FizzBuzz")
            elif (i%3 == 0): jj.append("Fizz")
            elif (i%5 == 0): jj.append("Buzz")
            else: jj.append(str(i))

        return jj
        