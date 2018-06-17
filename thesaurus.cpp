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

vs index;
map<string, int> rindex;


class union_find {
private:
	vi p; // parents
	vi s; // size of the set (only updated and valid for parents)

public:
	union_find(int n) {
		p.assign(n, 0);
		s.assign(n, 0);

		for (int i = 0; i < n; i++) {
			p[i] = i;
			s[i] = 1;
		}
	}

	int find_set(int i) {
		return (p[i] == i) ? i : (p[i] = find_set(p[i]));
	}

	bool is_same_set(int i, int j) {
		return (find_set(i) == find_set(j));
	}

	void union_set(int i, int j) {
		if (!is_same_set(i, j)) {
			int x = find_set(i);
			int y = find_set(j);

			if (index[x].size() < index[y].size()) {
				p[y] = x;
				s[x] += s[y];
			}
			else {
				p[x] = y;
				s[y] += s[x];
			}
		}
	}
};

int main() {

	int n, m; cin >> n >> m;
	vs s = vs(n);
	for (int i = 0; i < n; i++) {
		cin >> s[i];
	}

	index = vs();
	rindex = map<string, int>();

	union_find uf(10000);

	for (int i = 0; i < m; i++) {
		string a, b; cin >> a >> b;
		if (rindex.count(a) == 0) {
			rindex[a] = index.size();
			index.push_back(a);
		}
		if (rindex.count(b) == 0) {
			rindex[b] = index.size();
			index.push_back(b);
		}

		uf.union_set(rindex[a], rindex[b]);
	}

	int count = 0;
	for (string c : s) {
		if (rindex.count(c) == 0) {
			count += c.size();
		}
		else {
			string equiv = index[uf.find_set(rindex[c])];
			count += equiv.size();
		}
	}

	cout << count << endl;
}