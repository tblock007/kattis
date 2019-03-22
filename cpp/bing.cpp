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

class TrieNode {
public:
	int vd = 0;
	TrieNode* parent;
	map<char, TrieNode*> children;
};


class Trie {
public:

	Trie() {
		root = new TrieNode();
	}

	~Trie() {
		delete root;
	}

	int numPrefixes(string p) {
		TrieNode* curr = root;
		for (int i = 0; i < p.size(); i++) {
			char next = p[i];
			if (curr->children.count(next) == 0) {
				return 0;
			}
			curr = curr->children[next];
		}

		return curr->vd;
	}

	void add(string s) {
		TrieNode* curr = root;
		for (int i = 0; i < s.size(); i++) {
			char next = s[i];
			if (curr->children.count(next) == 0) {
				TrieNode* newNode = new TrieNode();
				newNode->parent = curr;
				curr->children[next] = newNode;
			}
			curr = curr->children[next];
		}

		while (curr != root) {
			curr->vd++;
			curr = curr->parent;
		}
	}

	TrieNode* root;
};



int main() {
	int n;
	cin >> n;

	Trie t;
	for (int i = 0; i < n; i++) {
		string s; cin >> s;
		cout << t.numPrefixes(s) << endl;
		t.add(s);
	}
}