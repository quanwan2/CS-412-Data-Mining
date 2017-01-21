# import library
import math
import numpy
import time
# set up directory
import os
os.chdir('/Users/quanwan2/Desktop/data-normalized-hw5')
# define our Point class
class Point:
    def __init__(self, coordinates, index):
        self.idx = index
        self.coord = coordinates
        self.cluster = 0
        self.idx = index

# load the txt file
ft = open('truth_normalized.txt', 'r')
point_num = int(ft.readline()[:-1])
truth_clus_num = int(ft.readline()[:-1])
counter = 0
true_list = []
for line in ft:
    info = line.split(',')
    pt = Point([float(info[0]),float(info[1])],counter)
    pt.cluster = int(info[2])
    counter+=1
    true_list.append(pt)
ft.close()

# We will begin bcube by using the results of the 3 previous generated files
# Subquestion1
f1 = open('step1.txt', 'r')
minPts = int(f1.readline()[:-1])
eps = float(f1.readline()[:-1])
output_clus_num = int(f1.readline()[:-1])
counter = 0
output1_list = []
for line in f1:
    info = line.split(',')
    pt = Point([float(info[0]),float(info[1])],counter)
    if int(info[2]) == 1:
        pt.cluster = 2
    elif int(info[2]) == 2:
        pt.cluster = 1
    elif int(info[2]) == 3:
        pt.cluster = 4
    else:
        pt.cluster = 0
    pt.cluster = int(info[2])
    counter+=1
    output1_list.append(pt)
f1.close()

output1_count = np.zeros(5)
for po in output1_list:
    output1_count[po.cluster]+=1
truth_count = np.zeros(5)
for po in true_list:
    truth_count[po.cluster]+=1

n = max(output_clus_num,truth_clus_num)+1
m = np.zeros([n,n])
for i in range(point_num):
    if(output1_list[i].cluster == true_list[i].cluster):
        m[output1_list[i].cluster,output1_list[i].cluster]+=1
    else:
        m[output1_list[i].cluster,true_list[i].cluster]+=1


precision = m[0,0]
recall = m[0,0]
for i in range(1,n):
    if(sum(m[:,i]) != 0):
        precision += math.pow(m[i,0],2)/sum(m[:,i])
        recall += m[i,0]
for j in range(1,n):
    if (sum(m[j,:]) != 0):
        precision += m[0,j]
        recall += math.pow(m[0,j],2)/sum(m[j,:])

for i in range(1,n):
    for j in range(1,n):
        if (sum(m[i,:]) != 0 and sum(m[:,j]) != 0):
            precision += math.pow(m[i,j],2)/sum(m[i,:])
            recall += math.pow(m[i,j],2)/sum(m[:,j])

precision/=point_num
recall/=point_num
print(precision)
print(recall)

# Subquestion2a
f2 = open('step2a.txt', 'r')
minPts = int(f2.readline()[:-1])
eps = float(f2.readline()[:-1])
output_clus_num = int(f2.readline()[:-1])
counter = 0
output2_list = []
for line in f2:
    info = line.split(',')
    pt = Point([float(info[0]),float(info[1])],counter)
    if int(info[2]) == 1:
        pt.cluster = 2
    elif int(info[2]) == 2:
        pt.cluster = 1
    elif int(info[2]) == 3:
        pt.cluster = 4
    elif int(info[2]) == 4:
        pt.cluster = 3
    else:
        pt.cluster = 0
    counter+=1
    output2_list.append(pt)
f2.close()

n = max(output_clus_num,truth_clus_num)+1
m = np.zeros([n,n])
for i in range(point_num):
    if(output2_list[i].cluster == true_list[i].cluster):
        m[output2_list[i].cluster,output2_list[i].cluster]+=1
    else:
        m[output2_list[i].cluster,true_list[i].cluster]+=1

import math
#outlier to outlier
precision = m[0,0]
recall = m[0,0]

#point to outlier
for i in range(1,n):
    #output has more clusters
    if(sum(m[:,i]) != 0):
        precision += math.pow(m[i,0],2)/sum(m[:,i])
        recall += m[i,0]

#outlier to point
for j in range(1,n):
    #truth has more clusters
    if (sum(m[j,:]) != 0):
        precision += m[0,j]
        recall += math.pow(m[0,j],2)/sum(m[j,:])


for i in range(1,n):
    for j in range(1,n):
        if (sum(m[i,:]) != 0 and sum(m[:,j]) != 0):
            precision += math.pow(m[i,j],2)/sum(m[i,:])
            recall += math.pow(m[i,j],2)/sum(m[:,j])

precision/=point_num
recall/=point_num
print(precision)
print(recall)



# Subquestion2b

f3 = open('step2b.txt', 'r')
minPts = int(f3.readline()[:-1])
eps = float(f3.readline()[:-1])
output_clus_num = int(f3.readline()[:-1])
counter = 0
output3_list = []
for line in f3:
    info = line.split(',')
    pt = Point([float(info[0]),float(info[1])],counter)
    if int(info[2]) == 1:
        pt.cluster = 4
    elif int(info[2]) == 2:
        pt.cluster = 1
    else:
        pt.cluster = 0
    counter+=1
    output3_list.append(pt)
f3.close()

n = max(output_clus_num,truth_clus_num)+1
m = np.zeros([n,n])
for i in range(point_num):
    if(output3_list[i].cluster == true_list[i].cluster):
        m[output3_list[i].cluster,output3_list[i].cluster]+=1
    else:
        m[output3_list[i].cluster,true_list[i].cluster]+=1

import math
#outlier to outlier
precision = m[0,0]
recall = m[0,0]

#point to outlier
for i in range(1,n):
    #output has more clusters
    if(sum(m[:,i]) != 0):
        precision += math.pow(m[i,0],2)/sum(m[:,i])
        recall += m[i,0]

#outlier to point
for j in range(1,n):
    #truth has more clusters
    if (sum(m[j,:]) != 0):
        precision += m[0,j]
        recall += math.pow(m[0,j],2)/sum(m[j,:])

for i in range(1,n):
    for j in range(1,n):
        if (sum(m[i,:]) != 0 and sum(m[:,j]) != 0):
            precision += math.pow(m[i,j],2)/sum(m[i,:])
            recall += math.pow(m[i,j],2)/sum(m[:,j])

precision/=point_num
recall/=point_num
print(precision)
print(recall)