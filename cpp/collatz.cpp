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


ll inline next(ll a) {
	if (a == 1) return 0;
	if (a % 2 == 0) {
		return (a / 2);
	}
	return (3 * a + 1);
}


int main() {
	ll a, b;
	while (cin >> a >> b && (a || b)) {
		ll oa = a;
		ll ob = b;
		map<ll, int> aseq;
		map<ll, int> bseq;

		int count = 0;
		aseq[a] = count;
		bseq[b] = count;
		if (a == b) {
			cout << oa << " needs 0 steps, " << ob << " needs 0 steps, they meet at " << a << endl;
		}
		else {
			while (1) {
				count++;
				a = next(a);
				b = next(b);
				aseq[a] = count;
				bseq[b] = count;

				if (aseq.count(b) > 0) {
					cout << oa << " needs " << aseq[b] << " steps, " << ob << " needs " << count << " steps, they meet at " << b << endl;
					break;
				}
				else if (bseq.count(a) > 0) {
					cout << oa << " needs " << count << " steps, " << ob << " needs " << bseq[a] << " steps, they meet at " << a << endl;
					break;
				}
			}
		}
	}
}