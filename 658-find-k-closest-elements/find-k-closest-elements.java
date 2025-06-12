class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> list = new ArrayList<>();
        for (int num : arr) {
            list.add(num);
        }

        // Sort by absolute difference, then value
        Collections.sort(list, (a, b) -> {
            int diffA = Math.abs(a - x);
            int diffB = Math.abs(b - x);
            if (diffA != diffB) return diffA - diffB;
            else return a - b;
        });

        // Pick first k elements
        List<Integer> result = list.subList(0, k);
        Collections.sort(result); // Return in ascending order
        return result;
    }
}
