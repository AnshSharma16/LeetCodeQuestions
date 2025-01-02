class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array to make use of two-pointer technique
        closest_sum = float('inf')  # Initialize closest_sum with a large value

        for i in range(len(nums) - 2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1  # Two pointers

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1  # Move left pointer to the right
                elif current_sum > target:
                    right -= 1  # Move right pointer to the left
                else:
                    return current_sum  # If exact match, return immediately

        return closest_sum  # Return the closest sum after all iterations
