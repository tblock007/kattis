#include <iostream>
#include <vector>
#include <set>
#include <tuple>

using namespace std;

typedef long long ll;
typedef tuple<int, int, int> iii;


int main() {
	
	int n, k; cin >> n >> k;
	set<iii> swaps;
	vector<int> c;
	for (int i = 0; i < k; i++) {
		int lt, h; cin >> lt >> h;
		swaps.emplace(-1 * h, lt, lt + 1);
	}

	for (int i = 0; i < n; i++) {
		c.push_back(i);
	}

	for (auto&& swap : swaps) {
		int l = get<1>(swap);
		int r = get<2>(swap);
		int temp = c[l];
		c[l] = c[r];
		c[r] = temp;
	}
	   	
	cout << c[0];
	for (int i = 1; i < n; i++) {
		cout << " " << c[i];
	}
	cout << endl;

	return 0;
}