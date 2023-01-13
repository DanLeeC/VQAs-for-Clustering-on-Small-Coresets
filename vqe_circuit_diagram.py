import vqe
import numpy as np
from math import pi
import pandas as pd

'''
Load data and build the problem graph
'''
data =  pd.read_csv('datasets/yeast.data', sep=r'\s+', header=None)

yeast_names = data[0]
data.drop(0, axis=1, inplace=True)

labels = data[9]
data.drop(9, axis=1, inplace=True)

num_points = 5
depth = 1

data = data.head(n=num_points)

#Convert to numpy matrix
data = data.to_numpy()

params = np.random.uniform(0, 2 * pi, 4 * num_points * (depth + 1))

problem_graph = vqe.data_to_graph(data)

circuit = vqe.vqe_circuit(problem_graph, params)

vqe.draw_circuit(circuit)
