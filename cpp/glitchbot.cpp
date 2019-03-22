#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
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


vi incx = { 0, 1, 0, -1 };
vi incy = { 1, 0, -1, 0 };


bool simulate(int x, int y, vs commands) {

	int a = 0;
	int b = 0;
	int dir = 0;

	for (int i = 0; i < commands.size(); i++) {
		if (commands[i] == "Forward") {
			a += incx[dir];
			b += incy[dir];
		}
		else if (commands[i] == "Right") {
			dir = (dir + 1) % 4;
		}
		else if (commands[i] == "Left") {
			dir = (dir + 3) % 4;
		}
	}

	//cout << "Ended up at " << a << " " << b << endl;

	if (a == x && b == y) {
		return true;
	}
	return false;
}


int main() {

	int x, y; cin >> x >> y;
	int n; cin >> n;

	vs commands = vs();

	for (int i = 0; i < n; i++) {
		string c; cin >> c;
		commands.push_back(c);
	}

	for (int i = 0; i < n; i++) {
		string orig = commands[i];

		commands[i] = "Forward";
		//cout << "trying " << i + 1 << " Forward" << endl;
		if (simulate(x, y, commands)) {
			cout << i + 1 << " Forward" << endl;
			return 0;
		}

		commands[i] = "Right";
		//cout << "trying " << i + 1 << " Right" << endl;
		if (simulate(x, y, commands)) {
			cout << i + 1 << " Right" << endl;
			return 0;
		}

		commands[i] = "Left";
		//cout << "trying " << i + 1 << " Left" << endl;
		if (simulate(x, y, commands)) {
			cout << i + 1 << " Left" << endl;
			return 0;
		}

		commands[i] = orig;
	}

	return 0;
}

