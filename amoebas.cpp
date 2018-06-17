#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
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


bool debug = true;
int m, n;
vvc grid;


void ff(int i, int j, char value)
{
	queue<ii> q = queue<ii>();
	q.push(ii(i, j));

	while (!q.empty())
	{
		// process this node and add neighbors
		int a = q.front().first;
		int b = q.front().second;
		q.pop();
		grid[a][b] = value;

		if (a > 0 && grid[a - 1][b] == '#') {
			q.push(ii(a - 1, b));
		}
		if (a < m - 1 && grid[a + 1][b] == '#') {
			q.push(ii(a + 1, b));
		}
		if (b > 0 && grid[a][b - 1] == '#') {
			q.push(ii(a, b - 1));
		}
		if (b < n - 1 && grid[a][b + 1] == '#') {
			q.push(ii(a, b + 1));
		}

		if (a > 0 && b > 0 && grid[a - 1][b - 1] == '#') {
			q.push(ii(a - 1, b - 1));
		}
		if (a > 0 && b < n - 1 && grid[a - 1][b + 1] == '#') {
			q.push(ii(a - 1, b + 1));
		}
		if (a < m - 1 && b > 0 && grid[a + 1][b - 1] == '#') {
			q.push(ii(a + 1, b - 1));
		}
		if (a < m - 1 && b < n - 1 && grid[a + 1][b + 1] == '#') {
			q.push(ii(a + 1, b + 1));
		}
	}
}

void print()
{
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cout << grid[i][j];
		}
		cout << endl;
	}
	cout << endl;
}


int main() {

	// amoebas

	cin >> m >> n;
	grid = vvc(m, vc(n, 0));

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			char c; cin >> c;
			grid[i][j] = c;
		}
	}

	int count = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (grid[i][j] == '#')
			{
				// we've hit a new cell
				count++;
				ff(i, j, count + '0');
			}
		}
	}

	cout << count << endl;
	

	return 0;
}