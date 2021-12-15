import java.util.*;

// There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

// A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

// Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

// Example 1:

// Illustration of graph
// Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
// Output: [2,4,5,6]
// Explanation: The given graph is shown above.
// Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
// Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
// Example 2:

// Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
// Output: [4]
// Explanation:
// Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

// Constraints:

// n == graph.length
// 1 <= n <= 104
// 0 <= graph[i].length <= n
// 0 <= graph[i][j] <= n - 1
// graph[i] is sorted in a strictly increasing order.
// The graph may contain self-loops.
// The number of edges in the graph will be in the range [1, 4 * 104].

class Solution802 {
    int[] connectToTerminals;
    boolean[] visited;

    public List<Integer> eventualSafeNodes(int[][] graph) {
        connectToTerminals = new int[graph.length];
        visited = new boolean[graph.length];
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < graph.length; i++) {
            if (graph[i].length == 0) {
                connectToTerminals[i] = 1;
            }
        }

        for (int i = 0; i < graph.length; i++) {
            if (connected(graph, i)) {
                res.add(i);
            }
        }
        return res;
    }

    public boolean connected(int[][] graph, int v) {
        if (connectToTerminals[v] == 1) {
            return true;
        } else if (connectToTerminals[v] == 2) {
            return false;
        }
        if (visited[v]) {
            return false;
        }

        visited[v] = true;
        for (int u: graph[v]) {
            if (!connected(graph, u)) {
                connectToTerminals[u] = 2;
                visited[v] = false;
                return false;
            }
        }

        visited[v] = false;
        connectToTerminals[v] = 1;
        return true;
    }
}

class Driver802 {
    public static void main(String[] args) {
        int[][] graph = {{1,2},{2,3},{5},{0},{5},{},{}};
        System.out.println(new Solution802().eventualSafeNodes(graph));
    }
}