import math
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for x in range(low,high+1 ):
            
            N=len(str(x))
            if N%2!=0:
                continue
            mid=N//2
            sumn = sum(int(d) for d in str(x)[:mid])
            summ = sum(int(d) for d in str(x)[mid:])
            if sumn==summ:
                count=count+1
        return count
