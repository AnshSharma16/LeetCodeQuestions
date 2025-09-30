import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Copy nums2 directly into nums1 after m elements
        System.arraycopy(nums2, 0, nums1, m, n);

        // Sort nums1
        Arrays.sort(nums1);
    }
}

