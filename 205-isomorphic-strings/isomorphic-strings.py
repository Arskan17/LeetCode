class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        record_of_ss_letters = {}
        record_of_ts_letters = {}

        for index, (letter_s, letter_t) in enumerate(zip(s, t)):
            if letter_s not in record_of_ss_letters:
                record_of_ss_letters[letter_s] = ""
            if letter_t not in record_of_ts_letters:
                record_of_ts_letters[letter_t] = ""

            record_of_ss_letters[letter_s] += str(index)
            record_of_ts_letters[letter_t] += str(index)

        for indexes in record_of_ss_letters.values():
            if indexes not in record_of_ts_letters.values():
                return False


        return True