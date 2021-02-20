#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <utility>
#include <unordered_map>
#include "vertex.h"
#include "iterator.h"
#include <string>

//typedef tri std::unordered_map<Edge, int, Edge>
//typedef std::pair<int, int> Edge;

class Edge
{
public:
	int first;
	int second;

	bool operator==(const Edge& other) const
	{
		return first == other.first;
	}
};

struct KeyHasher
{
	std::size_t operator()(const Edge& other) const 
	{
		return other.first;
	}
};

class Graph
{
private:
	
	std::vector<Vertex> vertices;
	std::unordered_map<Edge, int, KeyHasher> edges;
	//std::unordered_map<std::string, int> exemplu;
	std::vector<Vertex>::iterator find_vertex(int);
	Graph(const Graph&);
public:
	// Graph constructor
	Graph();
	
	Graph& operator = (const Graph&);

	bool is_edge(int out, int in) const;

	bool add_vertex(int label);
	bool remove_vertex(int label);

	bool add_edge(int out, int in);
	bool remove_edge(int out, int in);

	Iterator<int> get_outbound_edges_it(int label);
	Iterator<int> get_inbound_edges_it(int label);

	int size() const;

	Iterator<Vertex> get_graph_iterator() const;
	int get_edge_property(int out, int in);
	void set_edge_property(int out, int in, int val);
	
};

#endif
