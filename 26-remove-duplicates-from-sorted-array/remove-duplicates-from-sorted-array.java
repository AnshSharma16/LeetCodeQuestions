import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        int k = i + 1;

        // (Optional) Fill remaining with underscores for visualization
        String[] arrWithUnderscore = new String[nums.length];
        for (int idx = 0; idx < k; idx++) arrWithUnderscore[idx] = String.valueOf(nums[idx]);
        for (int idx = k; idx < nums.length; idx++) arrWithUnderscore[idx] = "_";

        System.out.println(Arrays.toString(arrWithUnderscore));
        return k;
    }
}