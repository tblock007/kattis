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

bool debug = true;

int bit_reverse(int i, int digits) {

	int result = 0;
	for (int d = 0; d < digits; d++)
	{
		if (i % 2 == 1) {
			result += 1;
		}
		i = i >> 1;
		result = result << 1;
	}
	result = result >> 1;
	return result;
}

int main() {

	// decisions
	
	
	int n; cin >> n;
	int nv = (1 << (n + 1));

	vi bdd(nv, -1); // one-indexed

	for (int i = (1 << n); i < nv; i++)
	{
		int index = i - (1 << n);
		int newindex = bit_reverse(index, n);
		cin >> bdd[newindex + (1 << n)];
	}

	int count = bdd.size() - 1;
	while (n > 0) {
		int start = (1 << n);
		int nc = start / 2;
		for (int i = 0; i < nc; i++) {
			if (bdd[start] != -1 && bdd[start + 1] != -1 && (bdd[start] == bdd[start + 1])) {
				// parent is at start / 2
				bdd[start / 2] = bdd[start];
				count -= 2;
			}
			start += 2;
		}
		n--;
	}
	
	cout << count << endl;

	


	return 0;
}