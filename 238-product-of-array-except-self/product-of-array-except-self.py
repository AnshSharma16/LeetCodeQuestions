class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=[1]*len(nums)
        left=1
        right=1
        for i in range(0,len(nums)):
            product[i]=left
            left*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            product[i] *= right
            right *= nums[i]
        
        return product
        