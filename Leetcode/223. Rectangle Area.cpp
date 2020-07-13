#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Find the total area covered by two rectilinear rectangles in a 2D plane.

// Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

// Rectangle Area

// Example:

// Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
// Output: 45
// Note:

// Assume that the total area is never beyond the maximum possible value of int.


 
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {

        if (C < E || G < A || D < F || H < B) {
            int area = (abs(A-C) * abs(B-D) + abs(E-G) * abs(F-H));
            return area;
        }

        // for row
        int row;
        if (A > E) {
            if (C > G) {
                row = G-A;
            } else {
                row = C-A;
            }
        } else {
            if (C > G) {
                row = G-E;
            } else {
                row = C-E;
            }
        }

        int col;
        if (B > F) {
            if (D > H) {
                col = H-B;
            } else {
                col = D-B;
            }
        } else {
            if (D > H) {
                col = H-F;
            } else {
                col = D-F;
            }
        }

        int cover_area = row*col;
        int area = (abs(A-C) * abs(B-D) - cover_area) + (abs(E-G) * abs(F-H) - cover_area) + cover_area;
        return area;
    }
};


int main() {
}
