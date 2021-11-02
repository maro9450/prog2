# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:43:48 2021

@author: Mattis
"""

from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future


def runner(n):
    print(f"Performing costly function {n}")
    pause(n)
    print(f"Function {n} has completed")
    
    
    
    
if __name__=="__main__":
    start = pc()
    
    with future.ProcessPoolExecutor() as ex:
        p = [5,4,3,2,1]
        results = ex.map(runner,p)
        
        for r in results:
            print(r)
    
    
    end = pc()
    print(f"Process took {round(end-start,2)} seconds")