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
	priority_queue<int, vi, less<int>> lh = priority_queue<int, vi, less<int >> ();
	priority_queue<int, vi, greater<int>> uh = priority_queue<int, vi, greater<int>>();

	int total = 0;
	string in;
	while (cin >> in) {
		if (in == "#") {

			cout << uh.top() << endl;
			uh.pop();
			total--;
		}
		else {
			int s = stoi(in);
			if (total == 0) {
				uh.push(s);
			}
			else {
				if (s < uh.top()) {
					lh.push(s);
				}
				else {
					uh.push(s);
				}
			}	
			total++;
		}

		// balance
		while (uh.size() > 0 && lh.size() < uh.size() - 1) {
			lh.push(uh.top()); uh.pop();
		}
		while (lh.size() > 0 && lh.size() > uh.size()) {
			uh.push(lh.top()); lh.pop();
		}
	}
}