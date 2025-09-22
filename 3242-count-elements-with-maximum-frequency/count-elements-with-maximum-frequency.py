class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={num : nums.count(num) for num in set(nums )}
        max_freq=max(d.values())
        summ=sum(v for v in d.values() if v==max_freq)
        return summ
        