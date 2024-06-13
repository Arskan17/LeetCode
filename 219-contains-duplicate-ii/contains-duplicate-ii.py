class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i, num in enumerate(nums):
        #     if num in nums[i+1:i+k+1]:
        #         return True

        # return False
        if len(nums)<2:
            return False

        position_records= {}
        for index, num in enumerate(nums):
            if num not in position_records:
                position_records[num] = []
            tempRecord = position_records[num]
            tempRecord.append(index)
            position_records[num] = tempRecord

        positions = [position for position in position_records.values()] # get back those indexes from the dictionart into a list

        distances = [(indexes[i+1]-indexes[i]) for indexes in positions for i in range(len(indexes)-1)] # if (indexes[i+1]-indexes[i]) <= k )
        for distance in distances:
            if distance <= k:
                return True
        
        return False
        