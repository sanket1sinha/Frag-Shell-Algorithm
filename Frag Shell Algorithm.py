
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import itertools
import re

k=int(input())
l=[]
while True:
    try:
        matrix=input()
        l.append(matrix)
    except EOFError:
         break   
l=[[i] for i in l]
a=[]
for i in l:
    m=[]
    m=[j for k in i for j in k.split()]
    a.append(m)
df = pd.DataFrame(a)
length_of_column=len(df.columns)
split_by=int(length_of_column/k)
dfs = np.split(df, [split_by], axis=1)
for i in range(len(dfs)):
    combinations=[]
    a=dfs[i].iloc[0]
    a=a.tolist()
    b=[a[i][0] for i in range(len(a))]
    y=sorted(b)
    for j in range(len(dfs[i])):
        lst=dfs[i].iloc[j]
        for k in range(1, len(lst)+1):
            c = [list(l) for l in itertools.combinations(lst, k)]
            combinations.extend(c)
    new_list=[' '.join(x) for x in combinations]
    length_of_string=[len(i) for i in new_list]
    length_of_string=set(length_of_string)
    length_of_string=list(length_of_string)
    length_of_string.sort()
    for j in length_of_string:
        one=[new_list[i] for i in range(len(new_list)) if len(new_list[i])==j]
        one_set=set(map(lambda x  : (x , list(one).count(x)) , one))
        one_sorted=sorted(one_set)
        one_sorted=sorted(one_sorted, key=lambda word:[b.index(i) for i in word[0][0]])
        if(y==b):
            one_sorted=sorted(one_sorted, key=lambda x: re.sub('[^A-Za-z]+', '', x[0]).lower())
        for k in range(len(one_sorted)):
            print(one_sorted[k][0],":",one_sorted[k][1])
    print("")

