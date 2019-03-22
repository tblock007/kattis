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

int n;
vvi dist;
map<ii, set<string>> pokemon;
vector<ii> stops;
vector<int> unneeded;


vvll memo;


// gives minimum distance of tour starts at i, visits all unvisited nodes (indicated by mask), and then returns to start
ll tsp(int i, int mask)
{
	//cout << "called for " << i << " of " << stops.size() << ", " << mask << ";" << endl;

	if (memo[i][mask] != -1)
	{
		return memo[i][mask];
	}
	

	//cout << " current pokemon are ";
	//for (string p : op) {
	//	cout << p << " ";
	//}
	//cout << endl;

	//// check whether current node even has new pokemon
	//bool nppresent = false;
	//for (string np : pokemon[stops[i]])
	//{
	//	if (op.find(np) == op.end()) {
	//		nppresent = true;
	//		break;
	//	}
	//}

	if (mask == ((1 << stops.size()) - 1))
	{
		return dist[i][0];
		//if (nppresent)
		//{
		//	// all nodes were visited, so simply return to start
		//	return dist[i][0];
		//}
		//else
		//{
		//	return dist[caller][0];
		//}
	}

	//if (!nppresent && i > 0) {
	//	cout << "DETERMINED NO NEW POKEMON AT NODE " << i << endl;
	//	return 1000000000000000;
	//}

	ll ans = 1000000000000000;
	for (int next = 0; next < stops.size(); next++)
	{
		if (next == i || ((1 << next) & mask) != 0)
		{
			continue;
		}

		if (unneeded[mask] & (1 << next) != 0) {
			mask = mask | (1 << next);
			continue;
		}
		
		// this is a candidate node
		ll temp = dist[i][next] + tsp(next, mask | (1 << next));
		if (temp < ans) {
			ans = temp;
		}
	}


	return memo[i][mask] = ans;
}

int main() {

	// pokemongogo
	
	cin >> n;
	pokemon = map<ii, set<string>>();
	stops = vii();
	stops.push_back(ii(0, 0));


	for (int i = 1; i <= n; i++) {
		int ri, ci; cin >> ri >> ci;
		string p; cin >> p;

		if (find(stops.begin(), stops.end(), ii(ri, ci)) == stops.end())
		{
			// new stop, so add it
			stops.push_back(ii(ri, ci));
		}

		pokemon[ii(ri, ci)].insert(p);
	}

	// compute distance matrix
	dist = vvi(stops.size(), vi(stops.size(), 0));
	for (int i = 0; i < stops.size(); i++) {
		for (int j = 0; j < stops.size(); j++) {
			int d = abs(stops[i].first - stops[j].first) + abs(stops[i].second - stops[j].second);
			dist[i][j] = d;
			dist[j][i] = d;
		}
	}

	// for each mask, store nodes that do not need to be visited
	unneeded = vi((1 << stops.size()) - 1, 0);
	for (int mask = 0; mask < ((1 << stops.size()) - 1); mask++)
	{
		// check the pokemon that belong in all the visited nodes
		set<string> op = set<string>();
		int tempmask = mask;
		int tempindex = 0;
		while (tempmask > 0) {
			if (tempmask % 2 == 1) {
				// we have visited this node, so collect the pokemon
					for (string poke : pokemon[stops[tempindex]]) {
						op.insert(poke);
					}
			}
			tempmask /= 2;
			tempindex++;
		}

		// iterate through the nodes to determine whether all pokemon are in op
		for (int node = 0; node < stops.size(); node++)
		{
			bool nppresent = false;
			for (string p : pokemon[stops[node]])
			{
				if (op.find(p) == op.end())
				{
					nppresent = true;
					break;
				}
			}

			if (!nppresent)
			{
				unneeded[mask] = unneeded[mask] | (1 << node);
			}
		}
	}

	memo = vvll(stops.size(), vll((1 << stops.size()), -1));
	cout << tsp(0, 1) << endl;




	return 0;
}