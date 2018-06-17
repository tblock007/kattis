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

	// anthony and diablo

	// largest area that can be enclosed by a given perimeter is a circle?

	double a, n; cin >> a >> n;
	double pi = atan(1.0) * 4.0;

	double r = n / 2.0 / pi;
	double maxarea = pi * r * r;

	if (maxarea - a > EPS)
	{
		cout << "Diablo is happy!" << endl;
	}
	else {
		cout << "Need more materials!" << endl;
	}
	

	return 0;
}

