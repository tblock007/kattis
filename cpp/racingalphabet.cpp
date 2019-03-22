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


vvd dist;


int c2v(char c) {
	if (c >= 'A' && c <= 'Z')
		return (int)(c - 'A');

	if (c == ' ')
		return 26;

	if (c == '\'')
		return 27;
}

int main() {

	// racingalphabet
	double pi = atan(1.0) * 4.0;
	double c = pi * 60.0;
	double dc = c / 28.0;
	dist = vvd(28, vd(28, 0.0));

	for (int i = 0; i < 28; i++) {
		for (int j = 0; j < 28; j++) {
			// compute distance from i to j around the circle
			int d = abs(i - j);
			if (d > 14) d = 28 - d;
			dist[i][j] = d * dc;
			dist[j][i] = d * dc;
		}
	}

	string line;
	int n;
	getline(cin, line);
	n = stoi(line);
	for (int i = 0; i < n; i++) {
		getline(cin, line);

		double ans = 1.0;
		for (int j = 1; j < line.size(); j++) {
			
			ans += dist[c2v(line[j])][c2v(line[j - 1])] / 15.0;
			ans += 1.0;
		}
		cout << fixed << setprecision(10) << ans << endl;
	}



	return 0;
}