#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import pandas as pd


if len(sys.argv) < 3:
        print("LM.py <orgfile> <anonyfile> ")
        exit()



names = (
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital-gain',
    'capital-loss',
    'hours-per-week',
    'native-country',
    'income',
)

categorical = set((
    'workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'sex',
    'native-country',
    'race',
    'income',
))

oldlist=[]
newlist=[]

ori_df = pd.read_csv(sys.argv[1], sep=", ", header=None, names=names, index_col=False, engine='python');
for column in ori_df.columns:
    if column in categorical : continue
    if column != names[0] : continue
    values = sorted(ori_df[column].unique())
    #print(len(values))  
    print(values)
    oldlist.append(values)

anony_df = pd.read_csv(sys.argv[2], sep=", ", header=None, names=names, index_col=False, engine='python');
for column in anony_df.columns:
    if column in categorical : continue
    if column != names[0] : continue
    values = sorted(anony_df[column].unique())
    print(values)
    newlist.append(values)



for i in range (0, len(oldlist)):
    old = oldlist[i]
    new = newlist[i]
    i=0
    generalize=0
    for anonyvalue in new :
        
        while True:
           if i == len(old) : break
           #print (anonyvalue)
           #print (old[i])
           if  anonyvalue <= old[i] :
               generalize+=1
               i=i+1
               #print("generalize")
           else:
               break
    
    print ("|average of N|")
    print (((generalize)/(len(new))-1)/(len(old)-1) )



