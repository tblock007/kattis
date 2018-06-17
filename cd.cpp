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

	int n, m;
	while (cin >> n >> m && (n || m)) {
		unordered_set<int> cds = unordered_set<int>();
		for (int i = 0; i < n; i++) {
			int temp; cin >> temp;
			cds.insert(temp);
		}

		int count = 0;
		for (int i = 0; i < m; i++) {
			int temp; cin >> temp;
			if (cds.count(temp) > 0) {
				count++;
			}
		}

		cout << count << endl;
	}
}