class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int sum=0;
        int count=0;
        int tempSum=0;
        for(int num:arr){
            sum+=num;
        }

        if(sum %3 !=0){
            return false;
        }

        int part=sum/3;

        for(int num:arr){
            tempSum+=num;
            if(tempSum==part){
                tempSum=0;
                count++;
            }
        }
        return count>=3;
    }
}