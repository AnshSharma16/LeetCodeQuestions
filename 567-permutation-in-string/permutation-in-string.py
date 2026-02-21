class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        w1 = Counter(s1)
        
        for i in range(len(s2)-len(s1)+1):
            w2= Counter(s2[i:i+len(s1)])
            if w1 == w2:
                return True
            
        return False
        