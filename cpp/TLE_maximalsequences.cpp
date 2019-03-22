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



int main() {

	// maximalsequences

	// read in all input
	int n; cin >> n;
	vi a = vi(n);

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	int q; cin >> q;
	vi s = vi(q);
	vsi b = vsi(q, si());

	for (int i = 0; i < q; i++) {
		int m; cin >> s[i] >> m; s[i]--;
		for (int j = 0; j < m; j++) {
			int temp; cin >> temp;
			b[i].insert(temp);
		}
	}

	// preprocess step: for each value in the sequence, obtain a set of its positions
	map<int, si> pos = map<int, si>();
	for (int i = 0; i < n; i++) {
		pos[a[i]].insert(i);
	}

	// now we can answer each query
	for (int i = 0; i < q; i++) {

		// check all positions of numbers NOT in the set b
		// find the smallest number of those positions
		int min = 1000000000;
		for (auto entry : pos) {
			if (b[i].find(entry.first) == b[i].end()) {
				for (int p : entry.second) {
					if (p < min && p >= s[i]) {
						min = p;
						break;
					}
				}
			}
		}

		if (min == 1000000000) {
			cout << n - s[i] << endl;
		}
		else {
			cout << min - s[i] << endl;
		}
	}




	return 0;
}