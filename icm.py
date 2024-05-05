import networkx as nx
import numpy as np
import random

class IndependentCascadeModel:
    def __init__(self, graph):
        self.graph = graph
        self.total_infected = 0
        self.spread_caused = {str(node): 0 for node in graph.nodes()}
        self.total_effect = {str(node): 0 for node in graph.nodes()}
        self.timestep = 0
        
    def simulate(self, seed):
        self.total_infected = 0
        curr_infected = np.zeros(len(self.graph.nodes()))
        prev_infected = np.zeros(len(self.graph.nodes()))

        prev_infected[int(seed)] = 1
        inactive = set()
        none_infected = False

        while not none_infected:
            none_infected = True
            probability = random.uniform(0, 1)

            #print(prev_infected)
            for node, state in enumerate(prev_infected):
                if state == 1:
                    predecessors = list(self.graph.predecessors(str(node)))

                    for predecessor in predecessors:
                        weight_data = self.graph.get_edge_data(predecessor, str(node))
                        if weight_data:
                            weight = weight_data['weight']
                            if int(predecessor) not in inactive:
                                if probability <= weight:
                                    curr_infected[int(predecessor)] = 1
                                    self.total_effect[str(node)] += 1
                                    none_infected = False
                    inactive.add(node)
                    self.total_infected += 1
            
            prev_infected = curr_infected.copy()
            curr_infected = np.zeros(len(self.graph.nodes()))
            
            self.timestep += 1

        return self.total_infected
    

    def run_simulation_all_nodes(self, n):
        results = {}
        for node in self.graph.nodes():
            total_infected_list = []
            for _ in range(n):
                self.total_infected = 0
                self.spread_caused = {str(n): 0 for n in self.graph.nodes()}
                self.timestep = 0
                total_infected = self.simulate(node)
                total_infected_list.append(total_infected - 1)
            avg = np.mean(total_infected_list)
            results[node] = avg

            
        return results





