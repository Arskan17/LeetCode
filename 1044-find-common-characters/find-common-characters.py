class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_counts = Counter(words[0])
        for word in words[1:]:
            char_counts &= Counter(word)  # Intersection of character counts
        return list(char_counts.elements())