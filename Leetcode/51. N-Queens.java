import java.util.ArrayList;
import java.util.List;

// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

// Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

// Example 1:


// Input: n = 4
// Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
// Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
// Example 2:

// Input: n = 1
// Output: [["Q"]]
 

// Constraints:

// 1 <= n <= 9

class Solution51 {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        backtrace(n, path, res);

        return res;
    }

    public void backtrace(int n, List<Integer> path, List<List<String>> res) {
        if (path.size() == n) {
            List<String> ans = new ArrayList<>();
            for (int i = 0; i < path.size(); i++) {
                StringBuilder b = new StringBuilder();
                int pos = path.get(i);
                for (int j = 0; j < n; j++) {
                    if (j != pos) {
                        b.append('.');
                    } else {
                        b.append('Q');
                    }
                }
                ans.add(b.toString());
            }
            res.add(ans);
            return;
        }

        for (int col = 0; col < n; col++) {
            int row = path.size();
            boolean valid = true;

            // check
            for (int i = 0; i < row; i++) {
                // same col
                if (col == path.get(i)) {
                    valid = false;
                    break;
                }
                // diagonal
                if (Math.abs(path.get(i) - col) == Math.abs(row - i)) {
                    valid = false;
                    break;
                }
            }

            if (!valid) {
                continue;
            }

            path.add(col);
            backtrace(n, path, res);
            path.remove(path.size() - 1);
        }
    }
}

class Driver51 {
    public static void main(String[] args) {
        Solution51 solution = new Solution51();

        int n = 7;
        System.out.println(solution.solveNQueens(n));
    }
}