import java.util.*;

// There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

// Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

// Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

// Example 1:


// Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
// Output: 3
// Explanation: The figure above describes the graph. 
// The neighboring cities at a distanceThreshold = 4 for each city are:
// City 0 -> [City 1, City 2] 
// City 1 -> [City 0, City 2, City 3] 
// City 2 -> [City 0, City 1, City 3] 
// City 3 -> [City 1, City 2] 
// Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
// Example 2:


// Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
// Output: 0
// Explanation: The figure above describes the graph. 
// The neighboring cities at a distanceThreshold = 2 for each city are:
// City 0 -> [City 1] 
// City 1 -> [City 0, City 4] 
// City 2 -> [City 3, City 4] 
// City 3 -> [City 2, City 4]
// City 4 -> [City 1, City 2, City 3] 
// The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

// Constraints:

// 2 <= n <= 100
// 1 <= edges.length <= n * (n - 1) / 2
// edges[i].length == 3
// 0 <= fromi < toi < n
// 1 <= weighti, distanceThreshold <= 10^4
// All pairs (fromi, toi) are distinct.


class Solution1334 {

    public int getCount(int start, int n, Map<Integer, List<int[]>> graph, int distanceThreshold) {
        int res = 0;
        int[] distances = new int[n];
        for (int i = 0; i < n; i++) {
            distances[i] = Integer.MAX_VALUE;
        }
        distances[start] = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> {
            return Integer.compare(distances[x], distances[y]);
        });
        pq.add(start);
        Set<Integer> sets = new HashSet<>();
        while (!pq.isEmpty()) {
            int u = pq.poll();
            if (sets.contains(u)) {
                continue;
            }
            sets.add(u);

            for (int[] pair: graph.getOrDefault(u, new ArrayList<>())) {
                int next = pair[0];
                int weight = pair[1];
                int this_dis = distances[u] + weight;
                if (this_dis < distances[next]) {
                    distances[next] = this_dis;
                    pq.add(next);
                }
            }
        }

        for (int i: distances) {
            if (i <= distanceThreshold) {
                res += 1;
            }
        }
        System.out.println(Arrays.toString(distances));
        return res - 1;
    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int minCount = n;
        int city = n - 1;
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] edge: edges) {
            if (!graph.containsKey(edge[0])) {
                graph.put(edge[0], new ArrayList<>());
            }
            graph.get(edge[0]).add(new int[] {edge[1], edge[2]});
            if (!graph.containsKey(edge[1])) {
                graph.put(edge[1], new ArrayList<>());
            }
            graph.get(edge[1]).add(new int[] {edge[0], edge[2]});
        }

        for (int i = 0; i < n; i++) {
            int count = getCount(i, n, graph, distanceThreshold);
            System.out.println("i: " + i + " count: " + count);
            if (count < minCount) {
                minCount = count;
                city = i;
            } else if (count == minCount && i > city) {
                city = i;
            }
        }
        return city;
    }
}

class Driver1334 {
    public static void main(String[] args) {
    }
}