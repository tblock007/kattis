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
#include <unordered_map>

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


string s;
int cl;
int ci;

void advci() {
	++ci;
	if (ci >= cl) ci = 0;
}

int main() {

	while (cin >> s && s != ".") {
		int len = s.size();
		cl = 1;
		ci = 0;

		int i = 0;
		while (i < s.size()) {
			//cout << "checking position " << i << " against " << ci << endl;
			if (s[i] != s[ci]) {
				//cout << "found mismatch; setting candidate to " << i + 1 - ci << endl;
				cl = i + 1 - ci;
				i = i - ci;
				ci = 0;
			}
			else {
				advci();
			}
			i++;
		}

		if (len % cl == 0) {
			cout << (len / cl) << endl;
		}
		else {
			cout << 1 << endl;
		}
	}
}