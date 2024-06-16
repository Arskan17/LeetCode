class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # inversedString = [s[index] for index in range(len(s)-1, -1, -1)]

        # for index, letter in enumerate(inversedString):
        #     s[index] = letter
        s.reverse()
        