class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if 'inf' in s.lower() or s.isalpha():
                return False
            if float(s) or float(s) >= 0:
                return True
        except:
            return False
        