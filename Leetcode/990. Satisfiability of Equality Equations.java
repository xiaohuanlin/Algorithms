import java.util.ArrayList;

// You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

// Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

// Example 1:

// Input: equations = ["a==b","b!=a"]
// Output: false
// Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
// There is no way to assign the variables to satisfy both equations.
// Example 2:

// Input: equations = ["b==a","a==b"]
// Output: true
// Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
// Example 3:

// Input: equations = ["a==b","b==c","a==c"]
// Output: true
// Example 4:

// Input: equations = ["a==b","b!=c","c==a"]
// Output: false
// Example 5:

// Input: equations = ["c==c","b==d","x!=z"]
// Output: true
 

// Constraints:

// 1 <= equations.length <= 500
// equations[i].length == 4
// equations[i][0] is a lowercase letter.
// equations[i][1] is either '=' or '!'.
// equations[i][2] is '='.
// equations[i][3] is a lowercase letter.


class Solution990 {
    private class UF {
        private int[] parent;
        private int[] size;
        public UF(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        };
        public int find(int root) {
            while (root != parent[root]) {
                parent[root] = parent[parent[root]];
                root = parent[root];
            }
            return root;
        };
        public void union(int i, int j) {
            i = find(i);
            j = find(j);
            if (i == j) {
                return;
            }

            if (size[i] < size[j]) {
                parent[i] = parent[j];
                size[j] += size[i];
            } else {
                parent[j] = parent[i];
                size[i] += size[j];
            }
        };
        public boolean isConnected(int a, int b) {
            return find(a) == find(b);
        };
    }

    public boolean equationsPossible(String[] equations) {
        ArrayList<int[]> problems = new ArrayList<int[]>();
        UF uf = new UF(26);

        for (String equation: equations) {
            int i = equation.charAt(0) - 'a';
            int j = equation.charAt(3) - 'a';
            if (equation.charAt(1) == '!') {
                int[] tmp = {i, j};
                problems.add(tmp);
            } else {
                uf.union(i, j);
            }
        }

        for (int[] problem: problems) {
            if (uf.isConnected(problem[0], problem[1])) {
                return false;
            }
        }
        return true;
    }
}

class Driver990 {
    public static void main(String[] args) {
        Solution990 solution = new Solution990();

        String[] e = {"a==b","b!=c","c==a"};
        System.out.println(solution.equationsPossible(e));
    }
}