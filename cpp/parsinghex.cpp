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



int main() {

	string line;
	while (getline(cin, line)) {
		for (int i = 0; i < line.size() - 2; i++) {
			if (line[i] == '0' && (line[i + 1] == 'x' || line[i + 1] == 'X')) {
				int s = i;
				int e = s + 2;
				while ((line[e] >= '0' && line[e] <= '9') || (line[e] >= 'A' && line[e] <= 'F') || (line[e] >= 'a' && line[e] <= 'f')) {
					e++;
				}
				if (e > (s + 2)) {
					string hex = line.substr(s, e - s);
					cout << hex << " " << strtoul(hex.c_str(), NULL, 0) << endl;
				}
			}
		}
	}
	
}