class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        sumw=sum(nums[:k])
        maxsum=sumw
        
        for right in range(k,len(nums)):
            sumw+=nums[right]
            sumw-=nums[right-k]
            maxsum=max(sumw,maxsum)

        return maxsum/k