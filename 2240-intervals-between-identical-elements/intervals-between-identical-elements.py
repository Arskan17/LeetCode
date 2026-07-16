class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        record = {}

        for i, n in enumerate(arr):
            if n not in record:
                record[n] = []
            tmp_list = record[n]
            tmp_list.append(i)
            record[n] = tmp_list

        intervals = [0]*len(arr)

        for n, indices in record.items():
            right_sum = sum(indices)
            right_count = len(indices)

            left_sum = 0
            left_count = 0

            for i in indices:
                right_sum -= i
                right_count -= 1

                left_distance = (left_count * i) - left_sum
                right_distance = right_sum - (right_count * i)

                intervals[i] = left_distance + right_distance

                left_sum += i
                left_count += 1

        return intervals
                
        