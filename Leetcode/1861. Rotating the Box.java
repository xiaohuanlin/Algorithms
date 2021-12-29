import java.util.*;

// You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

// A stone '#'
// A stationary obstacle '*'
// Empty '.'
// The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

// It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

// Return an n x m matrix representing the box after the rotation described above.

 

// Example 1:



// Input: box = [["#",".","#"]]
// Output: [["."],
//          ["#"],
//          ["#"]]
// Example 2:



// Input: box = [["#",".","*","."],
//               ["#","#","*","."]]
// Output: [["#","."],
//          ["#","#"],
//          ["*","*"],
//          [".","."]]
// Example 3:



// Input: box = [["#","#","*",".","*","."],
//               ["#","#","#","*",".","."],
//               ["#","#","#",".","#","."]]
// Output: [[".","#","#"],
//          [".","#","#"],
//          ["#","#","*"],
//          ["#","*","."],
//          ["#",".","*"],
//          ["#",".","."]]
 

// Constraints:

// m == box.length
// n == box[i].length
// 1 <= m, n <= 500
// box[i][j] is either '#', '*', or '.'.

class Solution1861 {
    public char[][] rotateTheBox(char[][] box) {
        int row = box.length;
        int col = box[0].length;
        char[][] res = new char[col][row];
        for (int i = row - 1; i >= 0; i--) {
            int count = 0;
            int start = 0;
            for (int j = 0; j <= col; j++) {
                if (j == col || box[i][j] == '*') {
                    // fill in the res
                    for (int k = start; k < j - count; k++) {
                        res[k][row - 1 - i] = '.';
                    }
                    for (int k = j - count; k < j; k++) {
                        res[k][row - 1 - i] = '#';
                    }
                    if (j != col) {
                        res[j][row - 1 - i] = '*';
                    }

                    start = j + 1;
                    count = 0;
                } else if (box[i][j] == '#') {
                    count++;
                }
            }
        }
        return res;
    }
}

class Driver1861 {
    public static void main(String[] args) {
        char[][] box = {{'#','.','#'}};
        System.out.println((new Solution1861()).rotateTheBox(box));
    }
}