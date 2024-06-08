class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters_values = [ord(letter) - 64 for letter in columnTitle]
        column_number = 0
        for value in letters_values:
            column_number = (column_number * 26) + value

        return column_number
        # 6 24 19 8 18 24 23