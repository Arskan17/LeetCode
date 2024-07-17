class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setRecord = {} # initalaize dictionary

        for index, elem in enumerate(nums):
            complement = target - elem # generating the other number
            if complement in setRecord: # if it's alreaddy in the dictionary, we can just give back the index
                return [setRecord[complement], index]
            else:
                setRecord[elem] = index # if it's not yet in the dictionary, put it in
        return
