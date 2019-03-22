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

	// dasort

	int p; cin >> p;
	while (p--) {
		int k; cin >> k;
		int n; cin >> n;

		vi s = vi(n);
		vi sorted = vi(n);

		for (int i = 0; i < n; i++) {
			int temp; cin >> temp;
			s[i] = temp; 
			sorted[i] = temp;
		}

		sort(sorted.begin(), sorted.end());

		int ifopis = -1;
		int oi = 0;
		bool found = true;
		while (found) {
			int cand = sorted[++ifopis];

			if (oi >= s.size()) {
				break;
			}

			while (s[oi++] != cand) {
				if (oi >= s.size()) {
					found = false;
					break;
				}
			}
		}
		cout << k << " " << sorted.size() - ifopis << endl;
	}

	return 0;
}