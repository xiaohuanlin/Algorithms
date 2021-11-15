import java.util.*;

// On an 8x8 chessboard, there can be multiple Black Queens and one White King.

// Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

 

// Example 1:



// Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
// Output: [[0,1],[1,0],[3,3]]
// Explanation:  
// The queen at [0,1] can attack the king cause they're in the same row. 
// The queen at [1,0] can attack the king cause they're in the same column. 
// The queen at [3,3] can attack the king cause they're in the same diagnal. 
// The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
// The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
// The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
// Example 2:



// Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
// Output: [[2,2],[3,4],[4,4]]
// Example 3:



// Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
// Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
 

// Constraints:

// 1 <= queens.length <= 63
// queens[i].length == 2
// 0 <= queens[i][j] < 8
// king.length == 2
// 0 <= king[0], king[1] < 8
// At most one piece is allowed in a cell.

class Solution1222 {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        int col = 8;
        List<List<Integer>> res = new LinkedList<>();
        int[] deltas = new int[8];
        for (int i = 0; i < deltas.length; i++) {
            deltas[i] = Integer.MAX_VALUE;
        }

        int kingPos = king[0] * col + king[1];

        for (int[] queen: queens) {
            int pos = queen[0] * col + queen[1];
            int delta = kingPos - pos;
            if (0 < delta) {
                if (delta <= king[1]) {
                    // left
                    deltas[3] = Math.min(deltas[3], delta);
                } else if (delta % (col - 1) == 0 && queen[1] > king[1]) {
                    // right-top
                    deltas[2] = Math.min(deltas[2], delta);
                } else if (delta % col == 0 && queen[1] == king[1]) {
                    // top
                    deltas[1] = Math.min(deltas[1], delta);
                } else if (delta % (col + 1) == 0 && queen[1] < king[1]) {
                    // left-top
                    deltas[0] = Math.min(deltas[0], delta);
                }
            } else if (delta < 0) {
                delta = -delta;
                if (delta < col - king[1]) {
                    // right
                    deltas[4] = Math.min(deltas[4], delta);
                } else if (delta % (col - 1) == 0 && queen[1] < king[1]) {
                    // left-bottom
                    deltas[5] = Math.min(deltas[5], delta);
                } else if (delta % col == 0 && queen[1] == king[1]) {
                    // bottom
                    deltas[6] = Math.min(deltas[6], delta);
                } else if (delta % (col + 1) == 0 && queen[1] > king[1]) {
                    // right-bottom
                    deltas[7] = Math.min(deltas[7], delta);
                }
            }
        }

        for (int i = 0; i < 8; i++) {
            if (deltas[i] == Integer.MAX_VALUE) {
                continue;
            }

            if (i >= 4) {
                deltas[i] = -deltas[i];
            }

            List<Integer> tmp = new LinkedList<>();
            tmp.add((kingPos - deltas[i]) / col);
            tmp.add((kingPos - deltas[i]) % col);
            res.add(tmp);
        }

        return res;
    }
}

class Driver1222 {
    public static void main(String[] args) {
        Solution1222 solution = new Solution1222();

        int[][] queens = {{0,1},{1,0},{4,0},{0,4},{3,3},{2,4}};
        int[] king = {0, 0};
        System.out.println(solution.queensAttacktheKing(queens, king));
    }
}