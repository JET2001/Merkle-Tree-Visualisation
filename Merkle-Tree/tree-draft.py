# This file creates a complete k-ary tree with labelled nodes in increasing order
# starting from 1 in Manim.
from manim import *
import networkx as nx 
import numpy as np
    
class Tree(Scene):
    def construct(self):
        ### Set some constants
        self.num_levels = 4
        self.k = 2 ## branching factor

        ########### Implementation
        self.vertices = list(range(1, self.get_label_of_last_node()+1))## assumes 1 is the root and indices follow after accordingly.
        # print(self.vertices)

        ## Edge list
        self.edges = self.compute_edges()

        ## Create the graph G
        g = Graph(self.vertices, self.edges, layout = 'tree', layout_scale = (5,2), labels = True, root_vertex = 1, vertex_config = {1: {"fill_color":RED}})

        self.play(Create(g), run_time = 2.5)
        self.wait(duration = 2)

    ### Custom utility function
    def compute_edges(self): ### Passes in the level order traversal of the tree
        '''
        Input: Level order traversal of the tree
        k: Branching factor (set to 2 as default)
        Output: A list of edges that each node is connected on the tree.
        '''
        edge_list = []
        for idx, v in enumerate(self.vertices):
            for child in range(1, self.k+1): # The children from 2k+1 to 3k will be the children of the node at index k.
                if (idx*self.k + child >= len(self.vertices)): 
                    break ## we hit a leaf node or the node has ran out of children.
                edge_list.append((v, self.vertices[idx*self.k+child]))
        print(edge_list)
        return edge_list
    
    ### Custom utility function to get the label of the last node.
    def get_label_of_last_node(self):
        '''
        Input:
        - num_levels: number of levels of the tree
        - k: branching factor of tree
        Output:
        - The number of the last node in the list (an integer)
        '''
        ## Since label of last node = total number of nodes = 1 + (k) + k^2 + ... + k^(n-1) = sum of GP
        return (self.k**self.num_levels-1)//(self.k-1)





