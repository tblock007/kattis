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

	// tetration
	double N; cin >> N;

	double lower = 0.0;
	double upper = 5.0;

	double el = pow(lower, N);
	double eu = pow(upper, N);
	double em = 1e300;

	double mid = (lower + upper) / 2.0;

	while (fabs(em - N) > 1e-7)
	{
		mid = (lower + upper) / 2.0;
		em = pow(mid, N);
		if (em > N) {
			upper = mid;
		}
		if (em < N) {
			lower = mid;
		}
	}

	cout << fixed << setprecision(6) << mid;



	return 0;
}

