import java.util.*;

// You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

// The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

// Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

// Example 1:



// Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
// Output: 20
// Explanation:

// We can connect the points as shown above to get the minimum cost of 20.
// Notice that there is a unique path between every pair of points.
// Example 2:

// Input: points = [[3,12],[-2,5],[-4,1]]
// Output: 18
// Example 3:

// Input: points = [[0,0],[1,1],[1,0],[-1,1]]
// Output: 4
// Example 4:

// Input: points = [[-1000000,-1000000],[1000000,1000000]]
// Output: 4000000
// Example 5:

// Input: points = [[0,0]]
// Output: 0
 

// Constraints:

// 1 <= points.length <= 1000
// -106 <= xi, yi <= 106
// All pairs (xi, yi) are distinct.

class Solution1584 {
    class Edge {
        int v;
        int u;
        int cost;
        Edge(int v, int u, int cost) {
            this.v = v;
            this.u = u;
            this.cost = cost;
        }
    }

    public int minCostConnectPoints(int[][] points) {
        PriorityQueue<Edge> pq = new PriorityQueue<>(new Comparator<Edge>() {

            @Override
            public int compare(Edge arg0, Edge arg1) {
                return Integer.compare(arg0.cost, arg1.cost);
            }
            
        });
        boolean[] marked = new boolean[points.length];
        int[][] graph = new int[points.length][points.length];

        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                graph[i][j] = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                graph[j][i] = graph[i][j];
            }
        }

        visit(graph, marked, pq, 0);
        int min = 0;
        while (!pq.isEmpty()) {
            Edge e = pq.poll();
            if (marked[e.v] && marked[e.u]) {
                continue;
            }
            min += e.cost;
            if (!marked[e.v]) {
                visit(graph, marked, pq, e.v);
            }
            if (!marked[e.u]) {
                visit(graph, marked, pq, e.u);
            }
        }
        return min;
    }

    public void visit(int[][] graph, boolean[] marked, PriorityQueue<Edge> pq, int v) {
        marked[v] = true;
        for (int i = 0; i < graph.length; i++) {
            if (!marked[i]) {
                pq.offer(new Edge(v, i, graph[v][i]));
            }
        }
    }
}

class Driver1584 {
    public static void main(String[] args) {
        int[][] points = {{0,0}, {2,2}, {3,10}, {5,2}, {7,0}};
        System.out.println(new Solution1584().minCostConnectPoints(points));
    }
}