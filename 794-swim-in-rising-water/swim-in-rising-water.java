import java.util.*;
class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        int left = grid[0][0], right = n * n - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (canReach(grid, mid, n)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean canReach(int[][] grid, int time, int n) {
        if (grid[0][0] > time) return false;

        boolean[][] visited = new boolean[n][n];
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        visited[0][0] = true;

        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0], y = curr[1];

            if (x == n - 1 && y == n - 1) return true;

            for (int[] d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && ny >= 0 && nx < n && ny < n &&
                    !visited[nx][ny] && grid[nx][ny] <= time) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }

        return false;
    }
}