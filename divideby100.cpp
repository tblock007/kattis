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

	// divideby100

	string n, m; cin >> n >> m;

	int dpshift = m.size() - 1;

	// find index of last non-zero
	int ilnz = -1;
	int numzeros = -1;
	for (int i = n.size() - 1; i >= 0; i--)
	{
		if (n[i] != '0') {
			ilnz = i;
			numzeros = n.size() - 1 - i;
			break;
		}
	}
	
	if (dpshift >= n.size())
	{
		// 0. case
		cout << "0.";

		int ztba = dpshift - n.size();
		for (int i = 0; i < ztba; i++) {
			cout << "0";
		}

		cout << n.substr(0, n.size() - numzeros);
	}
	else
	{
		if (dpshift <= numzeros)
		{
			// no decimal point
			cout << n.substr(0, n.size() - dpshift);
		}
		else {
			// need decimal point
			cout << n.substr(0, n.size() - dpshift) << "." << n.substr(n.size() - dpshift, dpshift - numzeros);
		}
		
	}


	return 0;
}

