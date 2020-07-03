#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

// In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

// Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

// Example 1:

// Input: "/home/"
// Output: "/home"
// Explanation: Note that there is no trailing slash after the last directory name.
// Example 2:

// Input: "/../"
// Output: "/"
// Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
// Example 3:

// Input: "/home//foo/"
// Output: "/home/foo"
// Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
// Example 4:

// Input: "/a/./b/../../c/"
// Output: "/c"
// Example 5:

// Input: "/a/../../b/../c//.//"
// Output: "/c"
// Example 6:

// Input: "/a//b////c/d//././/.."
// Output: "/a/b/c"

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> res;
        path.append("/");
        
        int start_index = 0;
        int count = 0;
        for (int i = 0; i < path.length(); i++) {
            if (path[i] == '/') {
                if (count != 0) {
                    string item = string(path, start_index, count);
                    if (item == ".") {
                    } else if (item == "..") {
                        if (!res.empty()) {
                            res.pop_back();
                        }
                    } else {
                        res.push_back(item);
                    }
                    count = 0;
                }
                start_index = i + 1;
                continue;
            }
            if (path[i] != '/') {
                count++;
            }
        }

        string result;
        for (int i = 0; i < res.size(); i++) {
            result += ("/" + res[i]);
        }

        if (result.empty()) {
            result = "/";
        }
        return result;
    }
};

int main() {
    Solution s;

    cout << s.simplifyPath("/a/b/..");
}