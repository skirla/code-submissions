class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = collections.Counter(nums)

        res = []
        sortedMap = sorted(countMap.items(), key = lambda x: x[1], reverse=True)

        counter = 0
        for val, i in sortedMap:
            res.append(val)
        return res[:k]



        
        
        
