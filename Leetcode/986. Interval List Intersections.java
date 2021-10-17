import java.util.*;

// You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

// Return the intersection of these two interval lists.

// A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

// The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

// Example 1:


// Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
// Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
// Example 2:

// Input: firstList = [[1,3],[5,9]], secondList = []
// Output: []
// Example 3:

// Input: firstList = [], secondList = [[4,8],[10,12]]
// Output: []
// Example 4:

// Input: firstList = [[1,7]], secondList = [[3,10]]
// Output: [[3,7]]
 

// Constraints:

// 0 <= firstList.length, secondList.length <= 1000
// firstList.length + secondList.length >= 1
// 0 <= starti < endi <= 10^9
// endi < starti+1
// 0 <= startj < endj <= 10^9
// endj < startj+1


class Solution986 {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int[][] allList = Arrays.copyOf(firstList, firstList.length + secondList.length);
        System.arraycopy(secondList, 0, allList, firstList.length, secondList.length);

        Arrays.sort(allList, (int[] a, int[] b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(a[1], b[1]);
        });

        int end = -1;
        List<int[]> res = new ArrayList<>();
        for (int[] pair: allList) {
            if (pair[0] > end) {
                end = pair[1];
            } else {
                int[] interval = {pair[0], Math.min(end, pair[1])};
                res.add(interval);
                end = Math.max(end, pair[1]);
            }
        }
        return (int[][])res.toArray(new int[0][]);
    }
}

class Driver986 {
    public static void main(String[] args) {
        Solution986 solution = new Solution986();

        int[][] first = {{5,10}};
        int[][] second = {{3,10}};
        System.out.println(Arrays.toString(solution.intervalIntersection(first, second)));
    }
}