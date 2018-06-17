#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
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



int main() {

	// fbiuniversal

	vi coeffs = { 2, 4, 5, 7, 8, 10, 11, 13 };
	map<char, int> v = map<char, int>();
	v['0'] = 0;
	v['1'] = 1;
	v['2'] = 2;
	v['3'] = 3;
	v['4'] = 4;
	v['5'] = 5;
	v['6'] = 6;
	v['7'] = 7;
	v['8'] = 8;
	v['9'] = 9;
	v['A'] = 10;
	v['B'] = 8;
	v['C'] = 11;
	v['D'] = 12;
	v['E'] = 13;
	v['F'] = 14;
	v['G'] = 11;
	v['H'] = 15;
	v['I'] = 1;
	v['J'] = 16;
	v['K'] = 17;
	v['L'] = 18;
	v['M'] = 19;
	v['N'] = 20;
	v['O'] = 0;
	v['P'] = 21;
	v['Q'] = 0;
	v['R'] = 22;
	v['S'] = 5;
	v['T'] = 23;
	v['U'] = 24;
	v['V'] = 24;
	v['W'] = 25;
	v['X'] = 26;
	v['Y'] = 24;
	v['Z'] = 2;

	int p; cin >> p;
	while (p--) {
		int k; cin >> k;
		string ucn; cin >> ucn;

		int sum = 0;
		for (int i = 0; i < ucn.size() - 1; i++) {
			sum += coeffs[i] * v[ucn[i]];
		}
		sum = sum % 27;

		if (v[ucn[ucn.size() - 1]] != sum) {
			cout << k << " Invalid" << endl;
		}
		else {
			ll value = 0;
			ll contr = 1;
			for (int i = ucn.size() - 2; i >= 0; i--) {
				value += (contr * v[ucn[i]]);
				contr *= 27;
			}
			cout << k << " " << value << endl;
		}
	}

	return 0;
}