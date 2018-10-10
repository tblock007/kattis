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
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<long long> vll;
typedef vector<vll> vvll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<vector<int>> vvi;

#define EPS 1e-12



void dfs(vvi const& al, vb& visited, vi& dist, vvi& children, vi& parent, int node, int depth) {
    dist[node] = depth;
    visited[node] = true;
    for (int i = 0; i < al[node].size(); i++) {
        if (!visited[al[node][i]]) {
            children[node].push_back(al[node][i]);
            parent[al[node][i]] = node;
            dfs(al, visited, dist, children, parent, al[node][i], depth + 1);
        }
    }
}

int lca(vi const& parent, int a, int b) {
    set<int> ancestors;
    ancestors.insert(a);
    while (a != 0) {
        a = parent[a];
        ancestors.insert(a);
    }

    if (ancestors.count(b) > 0) {
        return b;
    }
    while (b != 0) {
        b = parent[b];
        if (ancestors.count(b) > 0) {
            return b;
        }
    }
}

ll distance(vi const& dist, vi const& parent, int a, int b) {
    int ancestor = lca(parent, a, b);
    return (dist[a] - dist[ancestor]) + (dist[b] - dist[ancestor]) + 1;
}

int main() {

    int n; cin >> n;
    vvi al(n, vi());
    for (int i = 0; i < n - 1; i++) {
        int a, b; cin >> a >> b; a--; b--;
        al[a].push_back(b);
        al[b].push_back(a);
    }

    vvi children(n, vi());
    vi parent(n, -1);
    vi dist(n, -1);
    vb visited(n, false);
    dfs(al, visited, dist, children, parent, 0, 1);


    ll result = 0;
    for (int start = 1; start <= n; start++) {
        int end = start * 2;
        while (end <= n) {
            result += distance(dist, parent, start - 1, end - 1);
            end += start;
        }
    }
    cout << result << endl; 

}