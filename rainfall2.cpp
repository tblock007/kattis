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




int main() {

	double l, k, t1, t2, h;
	cin >> l >> k >> t1 >> t2 >> h;

	cout << fixed << setprecision(6);
	if (h < l) {
		cout << h << " " << h << endl;
	}
	else {
		double a = t1;
		double b = -1.0 * (h + t1 * k + t2 * k);
		double c = k * l;
		double det = b * b - 4 * a * c;
		double u = (-b + sqrt(det)) / 2.0 / a;

		if (h == l) {
			cout << h << " " << t1 * u << endl;
		}
		else {
			cout << t1 * u << " " << t1 * u << endl;
		}
	}
}