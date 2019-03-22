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


vvi al;
vi visited;
bool cycle;

void dfs(int root) {
	if (cycle) {
		return;
	}
	visited[root] = 1;
	for (int i = 0; i < al[root].size(); i++) {
		if (visited[al[root][i]] == 0) {
			dfs(al[root][i]);
		}
		else if (visited[al[root][i]] == 1) {
			cycle = true;
		}
	}
	visited[root] = 2;
}

int main()
{

	int n; cin >> n;

	set<string> seen = set<string>();
	vs lookup = vs();
	map<string, int> ilookup = map<string, int>();
	al = vvi();

	for (int i = 0; i < n; i++) {
		string a, b; cin >> a >> b;

		if (seen.count(a) == 0) {
			seen.insert(a);
			lookup.push_back(a);
			ilookup[a] = lookup.size() - 1;
			al.push_back(vi());
		}

		if (seen.count(b) == 0) {
			seen.insert(b);
			lookup.push_back(b);			
			ilookup[b] = lookup.size() - 1;
			al.push_back(vi());
		}

		al[ilookup[a]].push_back(ilookup[b]);
	}

	string q;
	while (cin >> q) {
		visited = vi(lookup.size(), 0);
		cycle = false;
		dfs(ilookup[q]);

		if (cycle) {
			cout << q << " safe" << endl;
		}
		else {
			cout << q << " trapped" << endl;
		}
	}

}