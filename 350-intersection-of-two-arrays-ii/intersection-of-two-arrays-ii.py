class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    result.append(nums1[i])
                    nums2[j] = float('-inf')  # Mark as used
                    break
        return result
        