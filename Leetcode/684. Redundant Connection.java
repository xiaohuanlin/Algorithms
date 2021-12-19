import java.net.ConnectException;
import java.util.*;

// In this problem, a tree is an undirected graph that is connected and has no cycles.

// You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

// Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

// Example 1:


// Input: edges = [[1,2],[1,3],[2,3]]
// Output: [2,3]
// Example 2:


// Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
// Output: [1,4]
 

// Constraints:

// n == edges.length
// 3 <= n <= 1000
// edges[i].length == 2
// 1 <= ai < bi <= edges.length
// ai != bi
// There are no repeated edges.
// The given graph is connected.

class Solution684 {
    class UF {
        int[] root;
        int[] size;

        UF(int n) {
            root = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                root[i] = i;
            }
        }

        boolean connected(int u, int v) {
            return find(u) == find(v);
        }

        void union(int u, int v) {
            int uRoot = find(u);
            int vRoot = find(v);
            if (uRoot == vRoot) {
                return;
            }
            if (size[uRoot] > size[vRoot]) {
                root[vRoot] = root[uRoot];
                size[uRoot] += size[vRoot];
            } else {
                root[uRoot] = root[vRoot];
                size[vRoot] += size[uRoot];
            }
        }

        int find(int v) {
            int iter = v;
            while (iter != root[iter]) {
                iter = root[iter];
            }

            while (v != root[v]) {
                int next = root[v];
                root[v] = iter;
                v = next;
            }
            return v;
        }
    }

    public int[] findRedundantConnection(int[][] edges) {
        UF uf = new UF(edges.length);
        for (int[] edge: edges) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            if (uf.connected(u, v)) {
                return edge;
            }
            uf.union(u, v);
        }
        return new int[] {};
    }
}

class Driver684 {
    public static void main(String[] args) {
        int[][] edges = {{1,2}, {1,3}, {2,3}};
        System.out.println((new Solution684()).findRedundantConnection(edges));
    }
}