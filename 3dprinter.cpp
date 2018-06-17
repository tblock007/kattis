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

	int n; cin >> n;

	int nbits = 0;
	int lsnz = -1;

	while (n > 0) {
		if (n % 2 == 1) {
			if (lsnz == -1) {
				lsnz = nbits;
			}
		}
		nbits++;
		n = n >> 1;
	}

	if (lsnz == nbits - 1) {
		cout << nbits << endl;
	}
	else {
		cout << nbits + 1 << endl;
	}

	
}