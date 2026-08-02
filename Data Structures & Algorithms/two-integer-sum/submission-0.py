class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for ind, num in enumerate(nums):
            diff = target-num

            if diff in prevMap:
                return [prevMap[diff], ind]
            prevMap[num] = ind

        return []