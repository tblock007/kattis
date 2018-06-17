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


int main() {

	// musical scales

	int n; cin >> n;

	map<string, int> index = map<string, int>();
	vs note = { "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#" };

	index["A"] = 0;
	index["A#"] = 1;
	index["B"] = 2;
	index["C"] = 3;
	index["C#"] = 4;
	index["D"] = 5;
	index["D#"] = 6;
	index["E"] = 7;
	index["F"] = 8;
	index["F#"] = 9;
	index["G"] = 10;
	index["G#"] = 11;

	vvi exclude = vvi(12, vi());

	exclude[0] = { 2, 4, 6, 9, 11 };
	exclude[1] = { 3, 5, 7, 10, 0 };
	exclude[2] = { 4, 6, 8, 11, 1 };
	exclude[3] = { 5, 7, 9, 0, 2 };
	exclude[4] = { 6, 8, 10, 1, 3 };
	exclude[5] = { 7, 9, 11, 2, 4 };
	exclude[6] = { 8, 10, 0, 3, 5 };
	exclude[7] = { 9, 11, 1, 4, 6 };
	exclude[8] = { 10, 0, 2, 5, 7 };
	exclude[9] = { 11, 1, 3, 6, 8 };
	exclude[10] = { 0, 2, 4, 7, 9 };
	exclude[11] = { 1, 3, 5, 8, 10 };

	vector<bool> possible = vector<bool>(12, true);

	for (int i = 0; i < n; i++) {
		string note; cin >> note;
		int noteindex = index[note];

		for (int e : exclude[noteindex])
		{
			possible[e] = false;
		}
	}


	int outputcount = 0;

	for (int i = 0; i < possible.size(); i++) {
		
		if (possible[i])
		{
			if (outputcount != 0)
				cout << " ";

			cout << note[i];
			outputcount++;
		}
	}

	if (outputcount == 0)
	{
		cout << "none";
	}

	return 0;
}

