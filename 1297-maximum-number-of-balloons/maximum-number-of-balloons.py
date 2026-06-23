class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        record = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for t in text:
            if t in record:
                m = record[t] + 1
                record[t] = m
            
        tmp = min(record["b"], record["a"], (record["l"]//2), (record["o"]//2), record["n"])

        return tmp
        