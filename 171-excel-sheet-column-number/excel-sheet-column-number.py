class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        for letter in columnTitle:
            value = ord(letter) - 64
            column_number = (column_number * 26) + value

        return column_number
        # 6 24 19 8 18 24 23