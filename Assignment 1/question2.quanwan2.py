# cs412 hw1
# Q2 - d
# @author quanwan2

dfile = open('/Users/quanwan2/Desktop/cs412_hw1/Data/vectors.txt')
num = 1
dfile.readline()
a = []
b = []
for line in dfile:
	if num == 1:
		a = line.split()
	else:
		if num == 2:
			b = line.split()
	num += 1

size = len(a)

def minkowski(h, a, b):
	sum = 0
	for i in range(size - 1):
		n1 = (int)(a[i+1])
		n2 = (int)(b[i+1])
		sum += abs((n1 - n2)**(h))
		
	#print sum
	prime = h**(-1)
	sum = (sum)**prime
	# print sum
	return sum

d2 = minkowski(2, a, b)
d3 = minkowski(3, a, b)
print 'When h = 2, minkowski_DISTANCE = ' + str(d2)
print 'When h = 3, minkowski_DISTANCE = ' + str(d3)


