class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_list= dict(Counter(nums))
        for key,freq  in freq_list.items():
            if freq>1:
                return True
        else:
            return False
        