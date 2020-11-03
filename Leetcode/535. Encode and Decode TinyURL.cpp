#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;


// Note: This is a companion problem to the System Design problem: Design TinyURL.
// TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

// Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Solution {
    unordered_map<string, string> maps;
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        string rand_v;
        do {
            rand_v = to_string(rand()); 
        } while (maps.find(rand_v) != maps.end());
        maps[rand_v] = longUrl;
        return rand_v;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return maps[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));


int main() {
    Solution s;
    string res;
    cout << (res = s.encode("asd")) << endl;
    cout << s.decode(res) << endl;
}