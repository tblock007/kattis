#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <stdio.h>

#define EPS 1e-9

using namespace std;

typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ll, ll> llll;
typedef vector<llll> vllll;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<set<int>> vsi;
typedef set<int> si;

#define UP 0x1
#define RIGHT 0x2
#define DOWN 0x4
#define LEFT 0x8

bool debug = true;

int dir;
int x, y;
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };

unordered_map<string, int> moved;
unordered_map<string, int> walls;

string pos(int x, int y) {
	return "(" + to_string(x) + "," + to_string(y) + ")";
}

string direction(int dir) {
	if (dir == 0) {
		return "up";
	}
	else if (dir == 1) {
		return "right";
	}
	else if (dir == 2) {
		return "down";
	}
	else if (dir == 3) {
		return "left";
	}
}

bool parse_input() {
	string input; cin >> input;
	if (input == "wall") {
		walls[pos(x, y)] = walls[pos(x, y)] | (1 << dir);
		return false;
	}
	else if (input == "ok") {
		x += dx[dir];
		y += dy[dir];
		return true;
	}
	else if (input == "solved" || input == "wrong") {
		exit(0);
	}

	return false;
}

void turn_right() {
	dir = (dir + 1) % 4;
	if (debug) cout << "Turned to face " << dir << endl;
}

void turn_left() {
	dir = (dir + 3) % 4;
	if (debug) cout << "Turned to face " << dir << endl;
}

// try going forward, returns true if successful
bool try_go_forward() {

	if (debug) cout << "Currently at position " << pos(x, y) << ", facing " << dir << endl;

	if ((moved[pos(x, y)] & (1 << dir)) || (walls[pos(x, y)] & (1 << dir))) {
		return false;
	}

	cout << direction(dir) << endl << flush;
	moved[pos(x, y)] = moved[pos(x, y)] | (1 << dir);
	return parse_input();
}

// try going right, returns true if successful
bool try_turn_go_right() {

	if (debug) cout << "Currently at position " << pos(x, y) << ", facing " << dir << endl;

	turn_right();

	if ((moved[pos(x, y)] & (1 << dir)) || (walls[pos(x, y)] & (1 << dir))) {
		turn_left();
		return false;
	}

	// otherwise, it is possible to go right according to our prior knowledge, so try it
	cout << direction(dir) << endl << flush;
	moved[pos(x, y)] = moved[pos(x, y)] | (1 << dir);

	bool success = parse_input();
	if (!success) {
		turn_left();
	}
	return success;
}

// try going left, returns true if successful
bool try_turn_go_left() {

	if (debug) cout << "Currently at position " << pos(x, y) << ", facing " << dir << endl;

	turn_left();

	if ((moved[pos(x, y)] & (1 << dir)) || (walls[pos(x, y)] & (1 << dir))) {
		turn_right();
		return false;
	}

	// otherwise, it is possible to go left according to our prior knowledge, so try it
	cout << direction(dir) << endl << flush;
	moved[pos(x, y)] = moved[pos(x, y)] | (1 << dir);

	bool success = parse_input();
	if (!success) {
		turn_right();
	}
	return success;
}





int main() {

	// amoebas

	moved = unordered_map<string, int>();
	walls = unordered_map<string, int>();
	dir = 0; // 0 is up, 1 is right, 2 is down, 3 is left
	x = 0; y = 0;

	// go up until wall is reached
	while (try_go_forward());

	turn_left();

	// there is now a wall on our right
	
	while (1) {
		if (try_turn_go_right()) {

		}
		else if (try_go_forward()) {

		}
		else if (try_turn_go_left()) {

		}
		else {
			// dead end, turn around so that left wall is on your right, then keep going
			turn_left();
			turn_left();
		}
	}

	return 0;
}