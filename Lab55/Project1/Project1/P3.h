#include <iostream> 
#include <list> 
using namespace std;

// A class that represents an undirected graph 
class Graph
{
	int V;    // No. of vertices 
	list<int> *adj;    // A dynamic array of adjacency lists 
public:
	// Constructor and destructor 
	Graph(int V) { this->V = V; adj = new list<int>[V]; }
	~Graph() { delete[] adj; }

	// function to add an edge to graph 
	void addEdge(int v, int w);

	// Prints greedy coloring of the vertices 
	void greedyColoring();
};