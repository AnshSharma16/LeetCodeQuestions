class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))  # Remove duplicates
        unique_nums.sort(reverse=True)  # Sort in descending order
        
        if len(unique_nums) < 3:
            return unique_nums[0]  # Return maximum if less than 3 unique numbers
        return unique_nums[2]  # Return third maximum


        