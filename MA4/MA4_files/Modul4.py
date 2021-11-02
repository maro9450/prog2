# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:35:58 2021

@author: Mattis
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def random_cords(N):
    X=[None]*N
    Y=[None]*N
    for n in range(N):
        X[n] = random.uniform(-1,1)
        Y[n] = random.uniform(-1,1)
    return [X,Y]

N=[1000,10000,100000]
approximations=[]
for n in N:
    plt.clf()
    C=np.array(random_cords(n))
    #indikator för huruvida innanför cirkelns radie
    inside = np.where(np.square(np.array(C[0]))+np.square(np.array(C[1])) < 1, 1, 0)
    n_c = np.sum(inside)
    approx = 4*n_c/n
    approximations.append(approx)
    
    
    
    #generera cirkel för plot
    cargs = np.linspace(0,2*np.pi,100)
    cx = np.cos(cargs)
    cy = np.sin(cargs)
    
    #plotta
    col_criteria = np.where(inside == 1, "red", "blue")
    plt.scatter(C[0],C[1], s=10, color=col_criteria)
    
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.title(f"N={n} : inside={n_c} : approximation={approx}")
    plt.plot(cx,cy, linewidth=0.7, c='black', linestyle='--')
    plt.show
    plt.savefig(f"pi approximation N {n}.png") 
    
print("n \t: approximation")
for e in range(len(N)):
    print(f"{N[e]} \t: {approximations[e]}")