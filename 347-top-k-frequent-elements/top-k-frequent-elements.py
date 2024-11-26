class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq, key=freq.get, reverse=True)

        return sorted_freq[0:k]
