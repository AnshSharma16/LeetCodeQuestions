import java.util.*;
class Solution {
    public int maxArea(int[] height) {
        int maxWater=0;
        int left=0;
        int right=height.length-1;

        while(left<right){
           int width=right-left;
            int h=Math.min(height[left],height[right]);
            int water=h*width;
            maxWater=Math.max(water,maxWater);

            if(height[left]<height[right]){
                left+=1;
            }
            else{
                right-=1;
            }

        }
        return maxWater;

    }
}