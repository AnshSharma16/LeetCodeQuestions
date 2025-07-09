class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int oldColor = image[sr][sc];
        if (oldColor == color) return image;

        dfs(image, sr, sc, oldColor, color);
        return image;
    }

    private void dfs(int[][] img, int x, int y, int oldColor, int newColor) {
        if (x < 0 || y < 0 || x >= img.length || y >= img[0].length) return;
        if (img[x][y] != oldColor) return;
        img[x][y] = newColor;

        dfs(img, x + 1, y, oldColor, newColor);
        dfs(img, x - 1, y, oldColor, newColor);
        dfs(img, x, y + 1, oldColor, newColor);
        dfs(img, x, y - 1, oldColor, newColor);
    }
}
