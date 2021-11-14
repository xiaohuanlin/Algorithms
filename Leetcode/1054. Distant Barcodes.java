import java.util.*;

// In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

// Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

// Example 1:

// Input: barcodes = [1,1,1,2,2,2]
// Output: [2,1,2,1,2,1]
// Example 2:

// Input: barcodes = [1,1,1,1,2,2,3,3]
// Output: [1,3,1,3,1,2,1,2]
 

// Constraints:

// 1 <= barcodes.length <= 10000
// 1 <= barcodes[i] <= 10000

class Solution1054 {
    public int[] rearrangeBarcodes(int[] barcodes) {
        int[] res = new int[barcodes.length];
        Map<Integer, Integer> counts = new HashMap<>();

        for (int barcode: barcodes) {
            counts.put(barcode, counts.getOrDefault(barcode, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(counts.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                return Integer.compare(o2.getValue(), o1.getValue());
            }
        });

        int index = 0;
        for (Map.Entry<Integer, Integer> entry: list) {
            int count = 0;
            while (index < barcodes.length && count < entry.getValue()) {
                res[index] = entry.getKey();
                index += 2;
                count++;
            }

            if (index >= barcodes.length) {
                index = 1;
                while (index < barcodes.length && count < entry.getValue()) {
                    res[index] = entry.getKey();
                    index += 2;
                    count++;
                }
            }
        }

        return res;
    }
}

class Driver1054 {
    public static void main(String[] args) {
        Solution1054 solution = new Solution1054();

        int[] b = {2,2,2,1,1,1};
        System.out.println(solution.rearrangeBarcodes(b));
    }
}