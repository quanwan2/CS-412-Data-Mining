# cs412 hw1
# Q1
# @author quanwan2

dfile = open('/Users/quanwan2/Desktop/Data/data.online.scores')

finalScores = []
size = 0
s = 0
for line in dfile:
	newLine = line.split()
	newScore = newLine[1]
	s += (float)(newScore)
	finalScores.append(newScore)
	size += 1

dfile.close()
finalScores.sort()
mean = (s)/(size)
variation = 0

for j in range(size):
	temp = (int)(finalScores[j])
	variation += (temp - mean)**2

variation = variation/(size - 1)
sigma = variation**(0.5)
z_scores = []
for k in range(size):
	temp = (int)(finalScores[j])
	z = (temp - mean)/sigma
	z_scores.append(z)

# print len(z_scores)
print 'Variance: ' + str(variation)
print('Mean: ' + str(mean))

