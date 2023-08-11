#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:20:02 2020

@author: jon-mpic
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('Dev_Dendro.xlsx', sheetname=0) # can also index sheet by name or fetch all sheets

Name = df['Name'].tolist()
d15N = df['d15N'].tolist()
stdev1 = df['stdev1'].tolist()
ncont = df['nmol/mg'].tolist()
stdev2 = df['stdev2'].tolist()

#Marl = df['Marl'].tolist()
#Marl_d15N = df['Marl_d15N'].tolist()
#stdev_M1 = df['stdev_M1'].tolist()
#Marl_ncont = df['Marl_ncont'].tolist()
#stdev_M2 = df['stdev_M2'].tolist()


fig = plt.figure(figsize=(10,5), dpi= 300)
axes = fig.add_axes([0,0,1,1])

plt.xticks(rotation = 90)
plt.yticks(np.arange(-3,8, step= 0.5))    #sets the y axis from 0 to 10

plt.tick_params(axis='x', which='major', labelsize=10)
plt.tick_params(axis='y', which='major', labelsize=10)

plt.xlabel('Sample Name')
plt.ylabel('d15N in \u2030 vs. air')
plt.title('Devonian Compilation - Dendrostella and Acanthophyllum Samples')


plt.ylim([-3, 8]) 
   
#plt.xlim([0, 52])

axes.plot(Name, d15N, 'o', color='k', label='d15N (\u2030)')
axes.errorbar(Name, d15N, yerr=stdev1, fmt='none', ecolor='k')
#axes.plot(PV6_year, PV6_ncont, '.-', color='red', label='nmol/mg')

axes2 = axes.twinx()
#
axes2.set_ylabel('N content nmol/mg')
#
axes2.plot(Name, ncont, 'o', color='red', label='nmol/mg')
axes2.errorbar(Name, ncont, yerr=stdev2, fmt='none', ecolor='r')


axes.legend(loc='upper left')
axes2.legend(loc='upper right')

axes.grid()

