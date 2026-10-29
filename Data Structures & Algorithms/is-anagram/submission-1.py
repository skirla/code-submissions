class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countsofS = {}
        for ch in s:
            countsofS[ch] = countsofS.get(ch,0) + 1
        
        countsofT = {}
        for ch in t:
            countsofT[ch] = countsofT.get(ch, 0) + 1
        
        
        for k, v in countsofT.items():
            if countsofS.get(k) != v:
                return False

        return True
        