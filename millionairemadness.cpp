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


bool check_path(const vvi& grid, int height) {
	int cc = 0;
	if (height < 0) {
		return false;
	}

	int n = grid.size();
	int m = grid[0].size();
	queue<ii> q = queue<ii>();
	vector<vb> visited = vector<vb>(n, vb(m, false));
	q.push(ii(0, 0));
	visited[0][0] = true;

	while (!q.empty()) {
		cc++;
		ii curr = q.front(); q.pop();


		if (curr.first == n - 1 && curr.second == m - 1) {
			return true;
		}

		if (curr.first > 0) {
			if (!visited[curr.first - 1][curr.second] && (grid[curr.first - 1][curr.second] - grid[curr.first][curr.second]) <= height) {
				q.push(ii(curr.first - 1, curr.second));
				visited[curr.first - 1][curr.second] = true;
			}
		}
		if (curr.first < n - 1) {
			if (!visited[curr.first + 1][curr.second] && (grid[curr.first + 1][curr.second] - grid[curr.first][curr.second]) <= height) {
				q.push(ii(curr.first + 1, curr.second));
				visited[curr.first + 1][curr.second] = true;
			}
		}
		if (curr.second > 0) {
			if (!visited[curr.first][curr.second - 1] && (grid[curr.first][curr.second - 1] - grid[curr.first][curr.second]) <= height) {
				q.push(ii(curr.first, curr.second - 1));
				visited[curr.first][curr.second - 1] = true;
			}
		}
		if (curr.second < m - 1) {
			if (!visited[curr.first][curr.second + 1] && (grid[curr.first][curr.second + 1] - grid[curr.first][curr.second]) <= height) {
				q.push(ii(curr.first, curr.second + 1));
				visited[curr.first][curr.second + 1] = true;
			}
		}
	}

	return false;
}


int main()
{

	int n, m; cin >> n >> m;

	vvi grid(n, vi(m, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> grid[i][j];
		}
	}

	int low = 0;
	int high = 1000000010;
	int mid = (low + high) / 2;

	bool ad = false;
	bool min = false;

	while (!(ad && min)) {
		ad = check_path(grid, mid);
		min = !check_path(grid, mid - 1);

		if (!ad) {
			low = mid;
			mid = (low + high) / 2;
		}
		else if (!min) {
			high = mid;
			mid = (low + high) / 2;
		}		
	}

	cout << mid << endl;


	return 0;
}