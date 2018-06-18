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
typedef unsigned long long ull;
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


int main()
{
	map<string, vi> m = map<string, vi>();
	int n; cin >> n;
	vs categ = vs();
	vi counts = vi(n, 0);
	for (int i = 0; i < n; i++) {
		string cat; cin >> cat; categ.push_back(cat);
		int w; cin >> w;
		for (int j = 0; j < w; j++) {
			string kw; cin >> kw;
			if (m.count(kw) == 0) {
				m[kw] = vi();
			}
			m[kw].push_back(i);
		}
	}


	string word;
	while (cin >> word) {
		if (m.count(word) > 0) {
			for (int i : m[word]) {
				counts[i]++;
			}
		}
	}

	int max = 0;
	for (auto count : counts) {
		if (count > max) max = count;
	}

	vs winners = vs();
	for (int i = 0; i < n; i++) {
		if (counts[i] == max) {
			winners.push_back(categ[i]);
		}
	}
	sort(winners.begin(), winners.end());

	for (string winner : winners) {
		cout << winner << endl;
	}
}