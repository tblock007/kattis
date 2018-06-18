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

using namespace std;

typedef long long ll;
typedef vector<long long> vll;
typedef vector<vll> vvll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<vector<int>> vvi;

#define EPS 1e-12

ll swaps;

void merge(vi& a, int ls, int le, int us, int ue) {
	vi scratch = vi(ue - ls + 1, 0);

	// merge into scratch
	int si = 0;
	int li = ls;
	int ui = us;
	while (li <= le || ui <= ue) {
		if (li <= le && ((ui > ue) || (a[li] < a[ui]))) {
			scratch[si] = a[li];
			li++;
			si++;
		}
		else {
			swaps += (le - li + 1);
			scratch[si] = a[ui];
			ui++;
			si++;
		}
	}

	// copy back to original vector in appropriate spot
	int ai = ls;
	for (int i = 0; i < scratch.size(); i++) {
		a[ai] = scratch[i];
		ai++;
	}
}

void ms(vi& a, int l, int r) {
	if (l == r) {
		return;
	}

	ms(a, l, (l + r) / 2);
	ms(a, (l + r) / 2 + 1, r);
	merge(a, l, (l + r) / 2, (l + r) / 2 + 1, r);
}

int main() {

	int n; cin >> n;
	vi a(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	swaps = 0;
	ms(a, 0, n - 1);

	cout << swaps << endl;


	return 0;
}