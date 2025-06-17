class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
       while(k>0){
          nums[0] *= (-1);
          Arrays.sort(nums);
          k--;
       } 

       int sum =0;
       for(int num : nums){
        sum += num;
       }

       return sum;
        
    }
}