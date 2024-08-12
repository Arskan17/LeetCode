class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        kybLayout = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        valid = []

        for word in words:
            for row in kybLayout:
                if all(letter in row.lower() for letter in word.lower()):
                    valid.append(word)
                    
        return valid