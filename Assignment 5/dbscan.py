# import library and set up directory
import math
import time
import os
os.chdir('/Users/quanwan2/Desktop/data-normalized-hw5')
# define our Point class
class Point:
    def __init__(self, coordinates, index):
        self.idx = index
        self.coord = coordinates
        self.visited = False
        self.noise = False
        self.cluster = 0

def eps_dist(p1, p2):
    d = 0
    for i in range(2):
        d+=math.pow((p1.coord[i]-p2.coord[i]),2)
    return math.sqrt(d)

def threshold(p_curr, p_list, eps, pts):
    count = 0
    for point in p_list:
        if (point.idx != p_curr.idx and eps_dist(p_curr, point) <= eps):
            count+=1
    return count >= pts

# open our file
f = open('data_normalized.txt', 'r')
# get the total number of points
point_num = int(f.readline()[:-1])
incre = 0
orig_list = []
for line in f:
    info = line.split(',')
    pt = Point([float(info[0]),float(info[1])],incre)
    incre+=1
    orig_list.append(pt)
f.close()

# open our file
f1 = open('truth_normalized.txt', 'r')
# get the total number of points
point_num = int(f1.readline()[:-1])
truth_list = []
incre = 0
f1.readline()
f1.readline()
for line in f1:
    info = line.split(',')
    pt = Point([float(info[0]),float(info[1])],incre)
    incre+=1
    truth_list.append(pt)
f1.close()

start = time.time()
# Set up params
epsilon = 0.065
minPts = 25
# Modified from CS411 team project
virgin_list = list(orig_list)
clus_idx = 0
while (len(virgin_list) != 0):
    point_curr = virgin_list.pop()
    if(point_curr.visited == True):
        continue

    point_curr.visited = True
    sub_list = []
    # get neighbors
    for point_sub in orig_list:
        if ((point_curr.idx != point_sub.idx) and (eps_dist(point_curr,point_sub) <= epsilon)):
            sub_list.append(point_sub)
    if(len(sub_list) >= minPts):        
        clus_idx+=1
        point_curr.cluster = clus_idx
        # traverse each point in N
        while(len(sub_list) != 0):
            point_deriv = sub_list.pop()
            if(point_deriv.visited == False):
                point_deriv.visited = True
                sub_sub_list = [];
                # add all neighbor points if they satisfiy our criteria
                for point_deriv_sub in orig_list:
                    if ((point_deriv_sub.idx != point_deriv.idx) and (eps_dist(point_deriv_sub,point_deriv) <= epsilon)):
                        sub_sub_list.append(point_deriv_sub)
                if(len(sub_sub_list) >= minPts):
                    for add_point in sub_sub_list:
                        sub_list.append(add_point)
            if(point_deriv.cluster == 0):
                point_deriv.cluster = clus_idx
    else:# it is a noise point
        point_curr.noise = True

end = time.time()
print(end - start)

for p in orig_list:
    print(p.idx, p.coord, p.visited, p.noise, p.cluster)
# plot the figures
import matplotlib.pyplot as plt
for p in truth_list:
    if p.cluster == 1:
        plt.plot(p.coord[0], p.coord[1],'go')
    if p.cluster == 2:
        plt.plot(p.coord[0], p.coord[1],'bo')
    if p.cluster == 3:
        plt.plot(p.coord[0], p.coord[1],'yo')
    if p.cluster == 4:
        plt.plot(p.coord[0], p.coord[1],'ro')
    else:
        plt.plot(p.coord[0], p.coord[1],'kx')
plt.show()
# write to file
f = open('step1.txt', 'w')
f.write('%d\n'%minPts)
f.write('%.3f\n'%epsilon)
f.write('%d\n'%clus_idx)
for point in orig_list:
    f.write('%.6f, %.6f, %d\n'%(point.coord[0],point.coord[1],point.cluster))
f.close()

