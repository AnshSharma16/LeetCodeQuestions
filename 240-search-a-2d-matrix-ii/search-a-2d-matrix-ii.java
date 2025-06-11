class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int n=matrix.length, m=matrix[0].length;
        int x=0,y=m-1;

        while(y>=0 && x<n){
            if (matrix[x][y]==target){
                return true;
            }
            else if (matrix[x][y]<target){
                x++;
            }
            else{
                y--;
            }
        }
        return false;
    }
}