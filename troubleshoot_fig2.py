#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:46:01 2021

@author: andrewlooka
"""

import numpy as np
import glob
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import multiprocessing
import os
'''
distances = np.arange(0,200, 10)
res = {}
mean_amp    = []
spread      = []
x           = []
for d in distances:
    
    if d in res:
        mean_amp.append( np.mean(res[d]) )
        spread.append(   np.std( res[d]) )
        x.append(d)
        
#for m in M:
 #   if m[1] >= 40:
  #      ax.plot(m[1], np.divide(m[0], mean_amp[3]), '.', ms=20, color='k', alpha=0.2)

#print x
#print mean_amp
mean_amp = np.divide(mean_amp, mean_amp[3])
'''



def get_max(f):
    
    x,y = np.loadtxt(f, unpack=True)
    
    m   = max(y[3300:-1])  
    
    path_file = os.path.split(f) 
    dist = int(path_file[1].split('_')[1])
    
    return [m, dist, x[3300:-1], y[3300:-1]]




fig, ax = plt.subplots(1,1, figsize=(6,8))
    
#files       = glob.glob(fString)
files = glob.glob('Results/Ca/ca*.out')

N           = len(files)

gradient    = [(1-1.0*x/(N-1), 0, 1.0*x/(N-1)) for x in range(N)]

res = {}

distances = np.arange(0,200, 10)

num_cores = multiprocessing.cpu_count() #int(np.ceil(multiprocessing.cpu_count() / 2))
M = Parallel(n_jobs=num_cores)(delayed(get_max)( f ) for f in files)

for m in M:
    
    for d in distances:
            
        #if m[1] > d-5 and m[1] < d+5:
            
            if d not in res:
                
                res[d] = []
                
            res[d].append(m[0])
            break
 
mean_amp    = []
spread      = []
x           = []
for d in distances:
    
    if d in res:
        mean_amp.append( np.mean(res[d]) )
        spread.append(   np.std( res[d]) )
        x.append(d)
        
for m in M:
    if m[1] >= 40:
        ax.plot(m[1], np.divide(m[0], mean_amp[3]), '.', ms=20, color='k', alpha=0.2)

#print x
#print mean_amp
mean_amp = np.divide(mean_amp, mean_amp[3])


#%%
res = {}
for m in M:
    
    for d in distances:
            
        if m[1] > d-5 and m[1] < d+5:
            
            if d not in res:
                
                print(d)
                res[d] = []
            res[d].append(m[0])
            print(res[d])
            print('about to break')
            break

#%%
res = {}
m_vals = []
for m in M:
    for d in distances:
        m_vals.append(m[1])
        if d not in res:
                
            res[d] = []
            
        res[d].append(m[0])
        break
        
print(m_vals)

#%%
for m in M:
    print(m[1])