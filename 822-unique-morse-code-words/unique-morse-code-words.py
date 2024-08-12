class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1

        morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        convertedWords = []

        for word in words:
            lword = word.lower() # convert word to lower case
            temp = "".join(morseAlphabet[ord(l)-97] for l in lword) # convert each character to morse equivalent and join them into a single string
            convertedWords.append(temp)

        return len(set(convertedWords))