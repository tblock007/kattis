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


int tobase(int d, int base)
{
	int result = 0;
	int contr = 1;
	while (d > 0) {
		int digit = d % 10;

		if (digit >= 8 && base == 8) {
			return 0;
		}

		d /= 10;

		result += contr * digit;
		contr *= base;
	}

	return result;
}


int main() {

	// whichbase

	int p; cin >> p;

	while (p--)
	{
		int k; cin >> k;
		int d; cin >> d;

		cout << k << " " << tobase(d, 8) << " " << d << " " << tobase(d, 16) << endl;
	}

	


	return 0;
}