class Solution:
    def maximumLengthSubstring(self, s: str) -> int: 
        def ismany(values):
            for i in values:
                if i > 2:
                    return False 
            return True
        
        maxi = -1 
        
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
               
                c = Counter(s[i:j + 1])
                if  ismany(c.values()):
                    maxi = max(maxi, len(s[i:j+1]))
        return maxi