import java.util.*;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = merge(nums1, nums2);
        int n = merged.length;
        
        if (n % 2 == 1) {
            return merged[n / 2]; // odd length → middle element
        } else {
            int mid1 = merged[n / 2 - 1];
            int mid2 = merged[n / 2];
            return (mid1 + mid2) / 2.0; // average of middle two
        }
    }
    
    private int[] merge(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        List<Integer> nums = new ArrayList<>();
        
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] <= nums2[j]) {
                nums.add(nums1[i]);
                i++;
            } else {
                nums.add(nums2[j]);
                j++;
            }
        }
        
        while (i < nums1.length) {
            nums.add(nums1[i]);
            i++;
        }
        
        while (j < nums2.length) {
            nums.add(nums2[j]);
            j++;
        }
        
        // Convert List<Integer> → int[]
        int[] merged = new int[nums.size()];
        for (int k = 0; k < nums.size(); k++) {
            merged[k] = nums.get(k);
        }
        
        return merged;
    }
}
