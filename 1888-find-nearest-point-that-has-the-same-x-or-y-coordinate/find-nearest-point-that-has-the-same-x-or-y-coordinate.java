class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int index=-1;
        int minManh=Integer.MAX_VALUE;
        for( int i=0;i<points.length;i++){
            int x1=points[i][0];
            int y1=points[i][1]; 
            int tmpManh=Math.abs(x-x1)+Math.abs(y-y1);
            if((x==x1 || y==y1) && tmpManh<minManh){
                minManh=tmpManh;
                index=i;
            }
        }
        return index;
    }
}