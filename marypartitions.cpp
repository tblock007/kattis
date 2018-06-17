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

vvll memob;

// returns number of partitions for n using only components only up to exponent e of base b
ll np(ll n, ll b, ll e)
{
	//cout << "called with " << n << " " << b << " " << e << endl;
	// base case
	if (e == 1) {
		return 1 + (n / b);
	}

	if (n == 0) {
		return 1;
	}

	if (n < 0) {
		return 0;
	}

	if (memob[n][e] != -1) {
		return memob[n][e];
	}


	ll hp = 1;
	for (int i = 0; i < e; i++) {
		hp *= b;
	}

	//cout << "highest power is " << hp << endl;

	ll result = 0;
	ll chp = 0;
	while (n - chp*hp >= 0)
	{
		result += np(n - chp*hp, b, e - 1);
		chp++;
	}

	return memob[n][e] = result;

}



int main() {

	// marypartitions

	int p; cin >> p;

	while (p--)
	{
		int k; cin >> k;
		ll m; cin >> m;
		ll n; cin >> n;

		memob = vvll(n + 1, vll(10, -1));

		cout << k << " " << np(n, m, 9) << endl;
	}

	


	return 0;
}