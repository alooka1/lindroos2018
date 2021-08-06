#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:09:45 2021

@author: andrewlooka
"""



import MSN_builder as build
import numpy as np
from neuron import h

par="./params_dMSN.json", \
                            run=None,       \
                            dynMod=1,       \
                            simDur=2000,    \
                            target=None,    \
                            not2mod=[]
    
print('iter:', run, target)



# initiate cell
cell    =   build.MSN(  params=par,                             \
                        morphology='latest_WT-P270-20-14ak.swc' )

    
# set cascade
casc = h.D1_reduced_cascade2_0(0.5, sec=cell.soma)


# specify pointer 
if target == 'control':
    target='Target1p'
#cmd         = 'pointer = casc._ref_'+target #WORKING
cmd         = 'casc._ref_'+target
import re
pointer =  re.compile(cmd)




'''
target = 'Target1p'
cmd     = 'pointer = casc._ref_'+target #WORKING
pointer =   casc._ref_Target1p
 

cmd = "casc._ref_" + target
'''

#%%
import re
regex = re.compile("Target1p")
print(regex)
print(type(regex))