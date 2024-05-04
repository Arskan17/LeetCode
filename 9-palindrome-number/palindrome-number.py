class Solution:
    def isPalindrome(self, x: int) -> bool:
        v = False
        if(x>=0): v = (int(str(x)[::-1]) == x)
        else: v = (reversed(str(x)) == str(x))
        return v