class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
         # Create a list of tuples (score, index) for sorting
        sorted_by_score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        # Initialize ranks dictionary for efficient lookup
        ranks = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

        # Assign ranks and maintain original order
        result = [""] * len(score)  # Initialize result list with empty strings
        for i, (_, score) in enumerate(sorted_by_score):
            rank = str(i + 1)  # Default rank (numeric)
            if i < 3:
                rank = ranks[i + 1]  # Assign medal ranks for top 3

            # Use the original index from the sorted list to place rank in the result list
            result[sorted_by_score[i][0]] = rank

        return result
