#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
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


int nb(int n) {
	int bits = 0;
	while (n > 0) {
		n = n >> 1;
		bits++;
	}
	return bits;
}


int main() {

	// rationalsequence3

	int p; cin >> p;
	while (p--) {
		int k; cin >> k;
		int n; cin >> n;

		int bits = nb(n);
		int num = 1;
		int denom = 1;

		vi dirs;
		for (int i = 0; i < bits - 1; i++) {
			int dir = n % 2;
			n = n >> 1;

			if (dir == 0) {
				// go left
				dirs.push_back(0);
			}
			else if (dir == 1) {
				// go right
				dirs.push_back(1);
			}
		}

		reverse(dirs.begin(), dirs.end());

		for (int d : dirs) {
			if (d == 0) {
				denom = num + denom;
			}
			else {
				num = num + denom;
			}
		}

		cout << k << " " << num << "/" << denom << endl;
	}
	


	return 0;
}