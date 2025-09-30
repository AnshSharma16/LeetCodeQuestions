import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[m + n];  // temporary array
        int i = 0, j = 0, k = 0;

        // Merge both arrays into temp[]
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                temp[k++] = nums1[i++];
            } else {
                temp[k++] = nums2[j++];
            }
        }

        // Copy remaining elements from nums1
        while (i < m) temp[k++] = nums1[i++];

        // Copy remaining elements from nums2
        while (j < n) temp[k++] = nums2[j++];

        // Copy temp back to nums1
        for (int idx = 0; idx < m + n; idx++) {
            nums1[idx] = temp[idx];
        }
    }
}
