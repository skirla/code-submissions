class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        alphaMap = {}
        for c in s:
           alphaMap[c] = alphaMap.get(c, 0) + 1
        
        for c in t:

            if c not in alphaMap or alphaMap.get(c, 0) == 0:
                return False

            if c in alphaMap:
                alphaMap[c] -= 1
        return True
        