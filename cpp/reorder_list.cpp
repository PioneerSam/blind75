#include <stdio.h>
#include <unordered_map>
#include <vector>
#include <queue>
#include <stack>


// Definition for a Node.
using namespace std;
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};


class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return nullptr;
        }

        queue<Node*> queue;
        queue.push(node);
        unordered_map<Node*,Node*> map;

        map[node] = new Node(node->val);

        while(!queue.empty()){
            Node* cur = queue.front();
            queue.pop();
            if(map.find(cur) == map.end()){
                map[cur] = new Node(cur->val);
            }

            for(int i=0;i<cur->neighbors.size();i++){
                Node* nei = cur->neighbors[i];
                if(map.find(nei) == map.end()){ //not found
                    queue.push(nei);
                    map[nei] = new Node(nei->val);
                }
                map[cur]->neighbors.push_back(map[nei]);
            }

        }

        return map[node];


        
    }
};


#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>

// --- If your file already has Node and Solution above, you can delete these includes
//     and keep only the main + printGraph bits. ---
//
// Assumes LeetCode-style Node:
// class Node {
// public:
//     int val;
//     std::vector<Node*> neighbors;
//     Node() : val(0), neighbors() {}
//     Node(int _val) : val(_val), neighbors() {}
//     Node(int _val, std::vector<Node*> _neighbors) : val(_val), neighbors(_neighbors) {}
// };
//
// Assumes you already defined:
// class Solution { public: Node* cloneGraph(Node* node); };

static void printGraph(Node* start) {
    if (!start) {
        std::cout << "(null)\n";
        return;
    }

    std::queue<Node*> q;
    std::unordered_set<Node*> seen;

    q.push(start);
    seen.insert(start);

    while (!q.empty()) {
        Node* cur = q.front();
        q.pop();

        std::cout << "Node val=" << cur->val << " @ " << cur << " -> neighbors: [ ";

        for (Node* nei : cur->neighbors) {
            std::cout << nei->val << "@" << nei << " ";
            if (!seen.count(nei)) {
                seen.insert(nei);
                q.push(nei);
            }
        }
        std::cout << "]\n";
    }
}

int main() {
    // Build a 4-node cycle: 1-2-3-4-1
    Node* n1 = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(4);

    n1->neighbors = {n2, n4};
    n2->neighbors = {n1, n3};
    n3->neighbors = {n2, n4};
    n4->neighbors = {n1, n3};

    std::cout << "Original graph:\n";
    printGraph(n1);

    Solution sol;
    Node* c1 = sol.cloneGraph(n1);

    std::cout << "\nCloned graph:\n";
    printGraph(c1);

    // Quick sanity checks
    std::cout << "\nSanity:\n";
    std::cout << "start pointers different? " << (c1 != n1 ? "YES" : "NO") << "\n";
    if (c1 && !c1->neighbors.empty()) {
        std::cout << "first neighbor pointer different? "
                  << (c1->neighbors[0] != n1->neighbors[0] ? "YES" : "NO") << "\n";
    }

    // Note: For a quick test program, it's fine to skip deletes.
    // In real code you'd free both graphs to avoid leaks.

    return 0;
}

