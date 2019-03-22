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



int main() {


	int t; cin >> t;

	while (t--) {
		int n; cin >> n;

		int a; cin >> a;
		int b;

		bool found = false;
		for (int i = 2; i <= n; i++) {

			cin >> b;
			if (b != a + 1 && !found) {
				cout << i << endl;
				found = true;
			}
			a = b;
		}
	}

	return 0;
}

