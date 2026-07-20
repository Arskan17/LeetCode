class Solution:
    def countSegments(self, s: str) -> int:
        previous_character_was_space = True

        num_of_segments = 0

        for letter in s:
            if ord(letter) != 32 and previous_character_was_space:
                num_of_segments += 1
                previous_character_was_space = False
            elif ord(letter) == 32:
                previous_character_was_space = True

        return num_of_segments