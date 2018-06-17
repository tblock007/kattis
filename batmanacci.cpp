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

vll fibs;

char solve(ll n, ll k) {

	if (n == 1) return 'N';
	if (n == 2) return 'A';

	if (n == 3) {
		if (k == 1) return 'N';
		if (k == 2) return 'A';
	}

	if (n > 91) {
		if (n % 2 == 0) {
			return solve(90, k);
		}
		else if (n % 2 == 1) {
			return solve(91, k);
		}
	}
	
	if (k <= fibs[n - 2]) {
		return solve(n - 2, k);
	}
	else if (k <= (fibs[n - 1])) {
		return solve(n - 3, k - fibs[n - 2]);
	}
	else {
		return solve(n - 2, k - fibs[n - 1]);
	}

}

int main()
{

	ll n, k; cin >> n >> k;

	fibs = vll();
	fibs.push_back(0);
	fibs.push_back(1);
	fibs.push_back(1);
	ll a = 1;
	ll b = 1;
	ll c = 0;
	while (c <= 1e18) {
		c = a + b;
		fibs.push_back(c);
		a = b;
		b = c;
	}
	
	cout << solve(n, k) << endl;

}