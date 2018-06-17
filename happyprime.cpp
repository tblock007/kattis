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


bitset<1000010> pf;

void sieve(ll n) {
	pf.set();
	pf[0] = pf[1] = false;
	for (ll i = 2; i <= n; i++) {
		if (pf[i]) {
			for (ll j = i * i; j <= n; j += i) {
				pf[j] = false;
			}
		}
	}
}

ll next(ll a) {
	ll result = 0;
	while (a > 0) {
		ll digit = (a % 10);
		result += digit * digit;
		a /= 10;
	}
	return result;
}

bool is_happy(ll a) {
	while (a != 1) {
		a = next(a);
		// all unhappy sequences eventually reach 4
		if (a == 4) {
			return false;
		}
	}
	return true;
}

int main()
{
	sieve(1000000);

	int n; cin >> n;
	for (int i = 1; i <= n; i++) {
		ll k, a; cin >> k >> a;

		cout << k << " " << a << " ";
		if (pf[a] && is_happy(a)) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}

		
	}


	return 0;
}