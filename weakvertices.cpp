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

	int n = 0; 
	while (cin >> n && n != -1) {
		
		vvi am = vvi(n, vi(n, 0));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> am[i][j];
			}
		}

		vi weaks = vi();
		for (int i = 0; i < n; i++) {
			bool weak = true;
			for (int j = 0; j < n; j++) {
				if (i != j && am[i][j] == 1) {
					for (int k = j + 1; k < n; k++) {
						if (k != i && am[i][k] == 1) {
							if (am[j][k] == 1) {
								weak = false;
							}
						}
					}
				}
			}

			if (weak) {
				weaks.push_back(i);
			}
		}

		bool first = true;
		for (int v : weaks) {
			if (!first) {
				cout << " ";
			}
			else {
				first = false;
			}
			cout << v;
		}
		cout << endl;
	}
}