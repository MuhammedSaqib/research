import numpy as np

from itertools import *
fname='outputs/out-1.txt'

with open(fname) as f:
    lines=f.readlines()
    
    



x=[]

myiter=lines.__iter__()

for i in myiter:
    xs=''
    if i[0]=='#':
        while i[0]=='#':
            xs+=i
            i=myiter.next()
        x.append(xs)


for i in xrange(len(x)):
    x[i]=x[i].replace('\n','')

n_samples=len(x)
n_param=len(x[0])
    
data=np.zeros((n_samples,n_param,3), dtype=np.bool)

    
for i in range(0,n_samples):
    for j in range(0,n_param):
        if x[i][j]=='#':
            data[i][j][0]=True
            data[i][j][1]=True
            data[i][j][2]=True
        elif( x[i][j]=='@'):
            data[i][j][0]=False
            data[i][j][1]=True
            data[i][j][2]=True
        elif(x[i][j]=='.'):
            data[i][j][0]=False
            data[i][j][1]=True
            data[i][j][2]=False
        elif (x[i][j]=='$'):
            data[i][j][0]=False
            data[i][j][1]=False
            data[i][j][2]=True
        elif (x[i][j]==' '):
            data[i][j][0]=False
            data[i][j][1]=False
            data[i][j][2]=False
