class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True
        
        jj = [j.lower() for j in s if j.isalnum()]

        n = len(jj)
        return all([jj[i]==jj[n-i-1] for i in range(n)])
