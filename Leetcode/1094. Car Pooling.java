import java.util.*;

// There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

// You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

// Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

// Example 1:

// Input: trips = [[2,1,5],[3,3,7]], capacity = 4
// Output: false
// Example 2:

// Input: trips = [[2,1,5],[3,3,7]], capacity = 5
// Output: true
// Example 3:

// Input: trips = [[2,1,5],[3,5,7]], capacity = 3
// Output: true
// Example 4:

// Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
// Output: true
 

// Constraints:

// 1 <= trips.length <= 1000
// trips[i].length == 3
// 1 <= numPassengersi <= 100
// 0 <= fromi < toi <= 1000
// 1 <= capacity <= 105

class Solution1094 {
    public boolean carPooling(int[][] trips, int capacity) {
        PriorityQueue<int[]> stops = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(a[1], b[1]);
        });

        for (int[] trip: trips) {
            stops.add(new int[] {trip[1], trip[0]});
            stops.add(new int[] {trip[2], -trip[0]});
        }

        int current = 0;
        while (!stops.isEmpty()) {
            int currentStop = stops.peek()[0];

            while (!stops.isEmpty() && stops.peek()[0] == currentStop) {
                current += stops.poll()[1];
            } 

            if (current > capacity) {
                return false;
            }
        }
        return true;
    }
}

class Driver1094 {
    public static void main(String[] args) {
        int[][] trips = {{9,3,4}, {9,1,7}, {4,2,4}, {7,4,5}};
        int capacity = 23;
        System.out.println((new Solution1094()).carPooling(trips, capacity));
    }
}