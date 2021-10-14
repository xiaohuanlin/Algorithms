import java.util.*;

// On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

// The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

// Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

// Example 1:


// Input: board = [[1,2,3],[4,0,5]]
// Output: 1
// Explanation: Swap the 0 and the 5 in one move.
// Example 2:


// Input: board = [[1,2,3],[5,4,0]]
// Output: -1
// Explanation: No number of moves will make the board solved.
// Example 3:


// Input: board = [[4,1,2],[5,0,3]]
// Output: 5
// Explanation: 5 is the smallest number of moves that solves the board.
// An example path:
// After move 0: [[4,1,2],[5,0,3]]
// After move 1: [[4,1,2],[0,5,3]]
// After move 2: [[0,1,2],[4,5,3]]
// After move 3: [[1,0,2],[4,5,3]]
// After move 4: [[1,2,0],[4,5,3]]
// After move 5: [[1,2,3],[4,5,0]]
// Example 4:


// Input: board = [[3,2,4],[1,5,0]]
// Output: 14
 

// Constraints:

// board.length == 2
// board[i].length == 3
// 0 <= board[i][j] <= 5
// Each value board[i][j] is unique.


class Solution773 {
    public int slidingPuzzle(int[][] board) {
        String start = transfer(board);
        Queue<String> q = new LinkedList<>();
        q.offer(start);
        
        Set<String> maps = new HashSet<>();
        maps.add(start);
        int steps = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String current = q.poll();
                if (current.equals("123450")) {
                    return steps;
                }
                for (String next: change(current)) {
                    if (maps.contains(next)) {
                        continue;
                    }
                    maps.add(next);
                    q.offer(next);
                }
            }
            steps++;
        }
        return -1;
    }

    public String transfer(int[][] board) {
        StringBuffer sBuffer = new StringBuffer();
        for (int[] row: board) {
            for (int c: row) {
                sBuffer.append(c);
            }
        }
        return sBuffer.toString();
    }

    public List<String> change(String s) {
        int start = s.indexOf('0');
        int x = start / 3;
        int y = start % 3;
        int[][] deltas = {{-1,0}, {0,-1}, {1,0}, {0,1}};
        List<String> res = new ArrayList<>();

        for (int[] delta: deltas) {
            int nextX = x + delta[0];
            int nextY = y + delta[1];
            if (nextX >= 0 && nextX < 2 && nextY >= 0 && nextY < 3) {
                char[] newString = s.toCharArray();
                char tmp = newString[start];
                newString[start] = newString[nextX * 3 + nextY];
                newString[nextX * 3 + nextY] = tmp;
                res.add(String.valueOf(newString));
            }
        }
        return res;
    }
}

class Driver773 {
    public static void main(String[] args) {
        Solution773 solution = new Solution773();

        int[][] board = {{1,2,3}, {4,0,5}};
        System.out.println(solution.slidingPuzzle(board));
    }
}