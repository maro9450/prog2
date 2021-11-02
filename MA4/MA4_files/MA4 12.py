# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:20:29 2021

@author: Mattis
"""

import random
import matplotlib.pyplot as plt
import math
import numpy as np
import functools
import time
import concurrent.futures as future


def random_points(n,d,r=1):         #skapar d listor med n slumptal unif(-1,1) vardera
    L=[[r*random.uniform(-1,1) for e in range(n)] for e in range(d)]
    return np.array(L)


def withindicator(V,r=1):
    #summera varje element från d dellistor i L och kolla om summan är mindre än radien
    L = [1 if sum(np.square(V[:,i])) <= r else 0 for i in range(V.shape[0])]
    return np.array(L)

def n_ball_volume(d,r=1):
    return r**d*np.pi**(d/2)/math.gamma(d/2+1)



def n_ball_approx(n,d,nruns=1,r=1):
    if nruns>1:
        processes=[]
        results=[]
        with future.ProcessPoolExecutor() as ex:
            for i in range(nruns):
                processes.append(ex.submit(n_ball_approx,n,d))
            for p in processes:
                results.append(p.result())
            return sum(results)/nruns    
    V = random_points(n,d)
    #modulu-funktion av array
    mod = lambda X : sum(np.square(X))
    #mappar samtliga koordinater till sin modulu
    Vmod = np.array(list(map(lambda i : mod(V[:,i]), range(n))))
    print(Vmod)
    #beräknar antalet punkter innanför radie
    n_ins = functools.reduce(lambda x,y : int(x)+int(y), map(lambda x : x<=r,Vmod))
    return 2**d*n_ins/n
    
    





def main():
    run1 = n_ball_approx(10**5,2)
    real1 = n_ball_volume(2)
    print(f"n=10^5, d=2 : approximation = {run1}, correct = {real1} : relative error = {abs(real1-run1)/real1}")
    
    
    run2 = n_ball_approx(10**5,11)
    real2 = n_ball_volume(11)
    print(f"n=10^5, d=11 : approximation = {run2}, correct = {real2} : relative error = {abs(real2-run2)/real2}\n")              
    
    
    #1.3
    start1 = time.perf_counter()
    run3 = n_ball_approx(10**7,11)
    stop1 = time.perf_counter()
    print(f"n=10^7 in 1 run, d=11 : Approximation = {run3} : Time: {stop1-start1} seconds : Relative error = {abs(real2-run3)/real2}\n")
    
    start2 = time.perf_counter()
    run4 = n_ball_approx(10**6,11,10)
    stop2 = time.perf_counter()
    print(f"n=10^7 in 10 runs, d=11 : Approximation = {run4} : Time: {stop2-start2} seconds : Relative error = {abs(real2-run4)/real2}\n")
    
    #resultat: multiprocessing ger snabbare resultat (26 sekunder vs 67 sekunder)
    
if __name__ == "__main__":
    main()