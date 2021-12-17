import java.util.*;

// Given a string s. Return all the words vertically in the same order in which they appear in s.
// Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
// Each word would be put on only one column and that in one column there will be only one word.

 

// Example 1:

// Input: s = "HOW ARE YOU"
// Output: ["HAY","ORO","WEU"]
// Explanation: Each word is printed vertically. 
//  "HAY"
//  "ORO"
//  "WEU"
// Example 2:

// Input: s = "TO BE OR NOT TO BE"
// Output: ["TBONTB","OEROOE","   T"]
// Explanation: Trailing spaces is not allowed. 
// "TBONTB"
// "OEROOE"
// "   T"
// Example 3:

// Input: s = "CONTEST IS COMING"
// Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 

// Constraints:

// 1 <= s.length <= 200
// s contains only upper case English letters.
// It's guaranteed that there is only one space between 2 words.

class Solution1324 {
    public List<String> printVertically(String s) {
        List<Integer> positions = new ArrayList<>();
        List<StringBuilder> res = new ArrayList<>();
        int index = 0;
        int column = 0;
        while (index < s.length()) {
            int row = 0;
            while (index < s.length() && s.charAt(index) != ' ') {
                if (res.size() <= row) {
                    res.add(new StringBuilder());
                    positions.add(-1);
                }
                int spaceNum = column - positions.get(row) - 1;
                for (int i = 0; i < spaceNum; i++) {
                    res.get(row).append(' ');
                }
                res.get(row).append(s.charAt(index));
                positions.set(row, column);
                index++;
                row++;
            }
            index++;
            column++;
        }
        List<String> ans = new ArrayList<>();
        for (StringBuilder sb: res) {
            ans.add(sb.toString());
        }
        return ans;
    }
}

class Driver1324 {
    public static void main(String[] args) {
        String s = "CONTEST IS COMING";
        System.out.println((new Solution1324()).printVertically(s));
    }
}