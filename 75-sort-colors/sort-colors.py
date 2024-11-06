class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            sorted_list = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            
            # Append any remaining elements
            sorted_list.extend(left[i:])
            sorted_list.extend(right[j:])
            
            return sorted_list
        
        # Sort nums using mergesort and replace its content in-place
        sorted_nums = mergesort(nums)
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]
