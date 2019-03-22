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


void dfs(vvi& al, vb& visited, int node) {
	visited[node] = true;
	for (int i = 0; i < al[node].size(); i++) {
		if (!visited[al[node][i]]) {
			dfs(al, visited, al[node][i]);
		}
	}
}

int main() {

	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vvi al(n, vi());
		vb visited = vb(n, false);

		int r; cin >> r;
		for (int i = 0; i < r; i++) {
			int a, b; cin >> a >> b;
			al[a].push_back(b);
			al[b].push_back(a);
		}

		int components = 0;
		for (int i = 0; i < n; i++) {
			if (!visited[i]) {
				components++;
				dfs(al, visited, i);
			}
		}

		cout << components - 1 << endl;
	}
}