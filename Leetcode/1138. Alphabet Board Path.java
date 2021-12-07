import java.util.*;

// On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

// Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



// We may make the following moves:

// 'U' moves our position up one row, if the position exists on the board;
// 'D' moves our position down one row, if the position exists on the board;
// 'L' moves our position left one column, if the position exists on the board;
// 'R' moves our position right one column, if the position exists on the board;
// '!' adds the character board[r][c] at our current position (r, c) to the answer.
// (Here, the only positions that exist on the board are positions with letters on them.)

// Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

// Example 1:

// Input: target = "leet"
// Output: "DDR!UURRR!!DDD!"
// Example 2:

// Input: target = "code"
// Output: "RR!DDRR!UUL!R!"
 

// Constraints:

// 1 <= target.length <= 100
// target consists only of English lowercase letters.

class Solution1138 {
    public Map<int[], String> maps = new HashMap<>();

    public String alphabetBoardPath(String target) {
        char start = 'a';
        StringBuilder sBuilder = new StringBuilder();
        for (char c: target.toCharArray()) {
            sBuilder.append(move(start - 'a', c - 'a'));
            start = c;
        }
        return sBuilder.toString();
    }

    public String move(int start, int end) {
        int[] pair = {start, end};
        if ((maps.containsKey(pair))) {
            return maps.get(pair);
        }
        StringBuilder sb = new StringBuilder();

        int x = (end / 5) - (start / 5);
        int y = (end % 5) - (start % 5);
        
        if (start == 25) {
            moveUpDown(x, sb);
            moveLeftRight(y, sb);
        } else {
            moveLeftRight(y, sb);
            moveUpDown(x, sb);
        }

        sb.append('!');
        maps.put(pair, sb.toString());
        return sb.toString();
    }

    public void moveUpDown(int x, StringBuilder sb) {
        for (int i = 0; i < Math.abs(x); i++) {
            if (x > 0) {
                sb.append('D');
            } else {
                sb.append('U');
            }
        }
    }

    public void moveLeftRight(int y, StringBuilder sb) {
        for (int i = 0; i < Math.abs(y); i++) {
            if (y > 0) {
                sb.append('R');
            } else {
                sb.append('L');
            }
        }
    }
}

class Driver1138 {
    public static void main(String[] args) {
        String target = "zdz";
        System.out.println((new Solution1138()).alphabetBoardPath(target));
    }
}