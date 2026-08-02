class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        frequencyMap = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c)-ord('a')] += 1
            
            key = tuple(count)

            if key not in frequencyMap:
                frequencyMap[key] = []
            frequencyMap[key].append(word)
        
        return list(frequencyMap.values())
