'''
Takes a small set of data of size n and produces a
diagram of the qaoa circuit ansatz for 2-means clustering
with p layers. The data is arbitrary as the goal is just
to produce a diagram of the circuit.
'''
from MaxCutQaoa import MaxCutQaoa, mean_clusters
import pandas as pd
import numpy as np
from math import pi

p = 1  #Number of layers of the circuit
n = 3   #Number of data points to use

#Load the data and remove unwanted columns.
#This is
data =  pd.read_csv('datasets/yeast.data', sep=r'\s+', header=None)

yeast_names = data[0]
data.drop(0, axis=1, inplace=True)

labels = data[9]
data.drop(9, axis=1, inplace=True)
data = data.head(n=n)
#Convert to numpy matrix
data = data.to_numpy()

#Initial circuit parameters
params = np.random.uniform(0, 2*pi, 2 * p)
#Prepare circuit and draw
clusters = mean_clusters(data)
clusters.qaoa.set_initial_params(params)
clusters.qaoa.prepare_circuit()
clusters.qaoa.show_circuit()
