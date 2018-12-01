#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:21:53 2018

@author: hannaholdorf
"""

#%% Graphs
# nodes = keys
# edges = values


graph = {
        "a":["b", "c"],
        "b":["d",],
        "c":["d"],
        "d":["e"],
        "e":[],
        "f":[]
        }

#%%

# Nodes 

def get_all_nodes(g):
    
    nodes = []
    
    for node in g:
        nodes.append(node)
    
    return nodes

get_all_nodes(graph)

# nodes/keys of a dictionary in one list with graph.key()

graph.keys()


#Edges
# a -> b
# a -> c
# b -> d ...

def get_all_edges(g):
    
    edges = []
    
    for node in g:
        for other_node in g[node]:
            edges.append(node + " ->" + other_node)
    
    return edges

get_all_edges(graph)

#%%
# edges/values of a dictionary in one list with graph.values()

graph.values()


#%% key with empty value and not listed as value of other key (HW Session14 - White Belt)

def non_connected(g):
    
    non_connected_nodes = []
    
    outgoing_edges = []
    
    for node in g:             # values of graph b,c,d,e
        for outgoing_edge in g[node]:
            outgoing_edges.append(outgoing_edge)
    
    for node in g:
        if g[node] == [] and node not in outgoing_edges:
            non_connected_nodes.append(node)
            
    return non_connected_nodes   


non_connected(graph)

#%% Fully Connected Graphs (HW Session14 - Blue Belt)

def fully_connected(g):
    
    nodes = list(g.keys())
    edges = 
    
    for node in g:
        for edge in g [node]:
            edges.append(edge)
    
    return len(edges) == nodes * (nodes -1)

#%%

def find_path(graph, start, end, path=[]):
    
    path += path + [start]           #append. adds to exisitng list 
                                    # path = path + [start] creates a new list 
    
    if start == end:
        return path 
    
    if start not in graph:
        return None 
    
    for conn in graph[start]:       # graph[start] list of outgoing edges
        
        if conn not in path:
            new_path = find_path(graph, conn, end, path)
            
            if new_path is not None:
                return new_path 
    
    return None


find_path(graph, "a", "a")

#%% 

ef find_all_paths(graph, start, end, path=[]):
    
    path += path + [start]           #append. adds to exisitng list 
                                    # path = path + [start] creates a new list 
    
    if start == end:
        return [path] 
    
    if start not in graph:
        return []                   # if there is no path retunf empty list
    
    paths = []
    
    for conn in graph[start]:       # graph[start] list of outgoing edges
        
        if conn not in path:
            new_paths = find_all_paths(graph, conn, end, path)   # list of lists
            print(new_paths)
            
            for new_path in new_paths:
                paths.append(new_path)
             
    
    return paths


find_all_paths(graph, "a", "d")


            
        
        
    


