import numpy as np
import networkx as nx

def diffusion_degree(graph):
    
    diff_degrees = {}

    for node in list(graph.nodes()):
        neighbors = list(graph.neighbors(node))
        
        
        # Iterate over neighbors and calculate their degrees
        for neighbor in neighbors:
            diff_degrees[str(node)] = graph.get_edge_data(neighbor,node)["weight"] * (1 + graph.reverse().degree(neighbor))

    return diff_degrees
            
            