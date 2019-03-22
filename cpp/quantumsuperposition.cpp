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
typedef vector<bool> vb;
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
typedef vector<set<int>> vsi;
typedef set<int> si;

vvi ral1;
vvi ral2;
vsi memo1;
vsi memo2;

si getlengths(vvi& ral, vsi& memo, int node)
{
	si result = si();

	if (node == 0)
	{
		result.insert(0);
		return result;
	}


	if (memo[node].find(-1) == memo[node].end())
	{
		return memo[node];
	}

	// combine the results from all parents
	for (int i = 0; i < ral[node].size(); i++)
	{
		int parent = ral[node][i];
		si r = getlengths(ral, memo, parent);
		for (int length : r)
		{
			result.insert(length + 1);
		}
	}

	return memo[node] = result;
}


int main() {

	// quantumsuperposition

	int n1, n2, m1, m2; cin >> n1 >> n2 >> m1 >> m2;
	ral1 = vvi(n1, vi());
	ral2 = vvi(n2, vi());
	memo1 = vsi(n1, si());
	memo2 = vsi(n2, si());

	for (int i = 0; i < n1; i++) {
		memo1[i].insert(-1);
	}
	for (int i = 0; i < n2; i++) {
		memo2[i].insert(-1);
	}

	for (int i = 0; i < m1; i++) {
		int a, b; cin >> a >> b; a--; b--;
		ral1[b].push_back(a);
	}

	for (int i = 0; i < m2; i++) {
		int a, b; cin >> a >> b; a--; b--;
		ral2[b].push_back(a);
	}
	
	// get possible lengths to last node
	si lengths1 = getlengths(ral1, memo1, n1 - 1);
	si lengths2 = getlengths(ral2, memo2, n2 - 1);

	// answer queries
	int nq; cin >> nq;

	while (nq--) {
		int q; cin >> q;

		// can q be expressed as a sum of one length from lengths1 and one from lengths2?
		bool found = false;
		for (int length : lengths1)
		{
			int target = q - length;

			if (lengths2.find(target) != lengths2.end())
			{
				found = true;
			}
		}

		if (found)
		{
			cout << "Yes" << endl;
		}
		else {
			cout << "No" << endl;
		}

	}

	return 0;
}

