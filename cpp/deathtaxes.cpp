#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <utility>
#include <sstream>
#include <string>
#include <bitset>
#include <algorithm>
#include <cmath>
#include <list>
#include <limits>
#include <functional>
#include <unordered_set>

#include <ctime>


#define INF 1000000000
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vvll> vvvll;
typedef priority_queue<int> pqi;
typedef priority_queue<ll> pqll;




int main() {

	int shares = 0;
	double avg = 1;
	double tb = 0;
	double tc = 0;
	string c;
	while (cin >> c) {
		if (c == "buy") {
			int x, y; cin >> x >> y;

			if (0) {
				tb += x;
				tc += (x * y);
				avg = tc / tb;
			}
			else {
				avg = (shares * avg + x * y) / (shares + x);
			}
			shares += x;
		}
		else if (c == "sell") {
			int x, y; cin >> x >> y;
			shares -= x;
		}
		else if (c == "split") {
			int x; cin >> x;
			shares *= x;
			avg /= x;
		}
		else if (c == "merge") {
			int x; cin >> x;
			shares /= x;
			avg *= x;
		}
		else if (c == "die") {
			int y; cin >> y;
			cout << fixed << setprecision(6);
			if (y > avg) {
				double profit = y - avg;
				cout << shares * (y - (profit * 0.3)) << endl;
			}
			else {
				cout << shares * y << endl;
			}
		}

		//cout << shares << " shares at " << avg << endl;
	}
}