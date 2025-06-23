class Solution(object):
    def countOdds(self, low, high):
        return (high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)

