class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # for i in range(len(s)):
        #     s_opposite = t[i]
        #     for j in range(i+1, len(t)):
        #         if (s[j] == s[i]) and (s_opposite != t[j]):
        #             return False
        #         if (s[j] != s[i]) and (s_opposite == t[j]):
        #             return False

        # return True



        record_of_ss_letters = {}
        record_of_ts_letters = {}

        for index, letter in enumerate(s):
            if letter not in record_of_ss_letters:
                record_of_ss_letters[letter] = ""
            record_of_ss_letters[letter] += str(index)

        for index, letter in enumerate(t):
            if letter not in record_of_ts_letters:
                record_of_ts_letters[letter] = ""
            record_of_ts_letters[letter] += str(index)

        for indexes in record_of_ss_letters.values():
            if indexes not in record_of_ts_letters.values():
                return False


        return True


        # return len(record_of_ss_letters) == len(record_of_ts_letters)

        # return len(set(s)) == len(set(t))