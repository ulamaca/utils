import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_swiss_roll
import itertools # for producing pairwise 2D latent plots
from mpl_toolkits.mplot3d import Axes3D # for 3D reconstruction


# All the functions to be devloped will be in the end put into a single plot_utils.py scripts
def swiss_roll_3dreconstruction(x, y, figsize=(10,5)):
    '''x: the input
       y: the target'''
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot('111', projection='3d')
    ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y, cmap=plt.cm.Spectral)
    

def swiss_roll_2dreconstructions(x, y, figsize=(14,3.5)):
    fig = plt.figure(figsize=figsize)
    plt.subplot(1,3,1)
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Spectral)    
    plt.subplot(1,3,2)
    plt.scatter(x[:, 0], x[:, 2], c=y, cmap=plt.cm.Spectral)
    plt.subplot(1,3,3)
    plt.scatter(x[:, 1], x[:, 2], c=y, cmap=plt.cm.Spectral)

def swiss_roll_2dlatent(x, y, figsize=(8,5)):   
    plt.figure(figsize=figsize)
    plt.scatter(x[:,0], x[:,1], c=y, cmap=plt.cm.Spectral)
    
def swiss_roll_2dlatents(x, y, figsize=(5,3)):
    '''
    two components: 
    1.) print the 2D scater if got only 2D input
    2.) print all pairwise scatter when got higer dimensional input (computational costly)
    '''
    dim_z = np.shape(x)[-1]
    list_of_dims = [d for d in range(dim_z)]
    for d1, d2 in itertools.combinations(list_of_dims, 2):
        plt.figure(figsize=figsize)
        plt.scatter(x[:,d1], x[:,d2], c=y, cmap=plt.cm.Spectral)
        plt.title('projection ({},{}): '.format(d1,d2))

# Todo: may create an grid-like plotting ops (cf. dSprite repo's examples)