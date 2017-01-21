# quanwan2

# Firstly, include the library needed.
import sys
from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser



# ------------- Helpers to be called in the Apriori Algorithm --------------
def get_Subsets(current):
	
	# ret = set()
	# for i, item in enumerate(current):
	#     for item in  combinations(current, i + 1)
	#     ret.add(*temp)
	# return ret
	return chain(*[combinations(current, i + 1) for i, a in enumerate(current)])
# Keep the items with support >= min_support in our item set
def Prune(min_support, item_Set, dataList, freq):
	
	# The set consists of all wanted items
	ret_Set = set()
	# Helper dictionary to store count for each item
	tmp_dict = defaultdict(int)
	for item in item_Set:
		for record in dataList:
			if item.issubset(record):
				tmp_dict[item] = tmp_dict[item] + 1
				freq[item] = freq[item] + 1
	

	for item, count in tmp_dict.items():
		relative_support = float(count)/(len(dataList))
		if relative_support >= min_support:
			ret_Set.add(item)

	return ret_Set

# Do self_join to increment size by 1
def self_joining(item_Set, l):
	ret_Set = set()
	for i in item_Set:
		for j in item_Set:
			if(len(i.union(j)) == l):
				ret_Set.add(i.union(j))
	return ret_Set

# Convert the data to transaction lists and item set.
def convert_to_list(indata):
	# The set consists of all items
	item_Set = set()
	# The list consists of all records(rows) from the original data
	dataList = list()
	for record in indata:
		tmp = record
		dataList.append(frozenset(record))
		for i in record:
			item_Set.add(frozenset([i]))
	return item_Set, dataList

# Import the data, which is separated by space in each row
def import_Data(filename):
	data = open(filename,'rU')
	for line in data:
		line = line.strip()                         
		record = frozenset(line.split())
		# yield the data keeps 'for' happy
		yield record

def writeFile(arg1, arg2):
	# with open('/Users/quanwan2/Desktop/data/max-0.txt', 'w') as theFile:
	with open('/Users/quanwan2/Desktop/data/max-4.txt', 'w') as theFile:
	# with open('/Users/quanwan2/Desktop/data/max-2.txt', 'w') as theFile:
	# with open('/Users/quanwan2/Desktop/data/max-3.txt', 'w') as theFile:
	# with open('/Users/quanwan2/Desktop/data/max-4.txt', 'w') as theFile:
		for item_set, support in reversed(sorted(arg1, key=lambda (item_set, support): support)):
			if support > 0:
				words = []
				theFile.write("%d\t" % (support))
				for item in item_set:
					tmp = arg2[item]
					words.append(tmp)
				for word in words:
					theFile.write("%s " % str(word))
				theFile.write("\n")
	theFile.close()

# def changeFormat():
# 	with open('/Users/quanwan2/Desktop/data/pattern-0.txt', 'w') as theFile:
# 		for line in theFile:
# 			if '"' + '' in line:
# 				line = line.replace('"' + '', '')
# 				theFile.write(line)
		# print "%d   %s" % (support, str(word).strip('[]'))

# ---------------------- Apriori Algorithm ------------------------
def Apriori(filename, min_support, min_Confidence):
	

	output = dict()
	association = dict()
	freq = defaultdict(int)
	indata = import_Data(filename)
	item_Set, dataList = convert_to_list(indata)
	back_to_words = dict()
	vocal = open('/Users/quanwan2/Desktop/data/vocab.txt')
	for line in vocal:
		line.strip()
		tmp = line.split()
		index = tmp[0]
		back_to_words[index] = tmp[1]

	ONE_item_set = Prune(min_support, item_Set, dataList, freq)	
	current = ONE_item_set
	l = 2
	while(current):
			output[l - 1] = current
			current = self_joining(current, l)
			tmp = Prune(min_support, current, dataList, freq)
			current = tmp
		# Increment the size and repeat
			l = l + 1


	ret1 = []
	for k, v in output.items():
		ret1.extend([(tuple(item), freq[item])
					for item in v])

	
	# changeFormat()
	ret2 = []
	ret3 = []
	for item_set, support in reversed(sorted(ret1, key=lambda (item_set, support): support)):
		set1 = set(item_set)
		count = support
		for item_set1, support1 in reversed(sorted(ret1, key=lambda (item_set, support): support)):
			set2 = set(item_set1)
			count1 = support1
			if(set1.issubset(set2) and set2.difference(set1) > 0):
				set1 = set2
				support = support1
		ret3.extend([(tuple(set1), support)])
	
	ret4 = set()
	ret5 = []
	ret6 = []
	for item_set, support in ret3:
		if (item_set, support) not in ret4:
			ret4.add((tuple(item_set), support))
	for item in ret4:
		ret5.extend([item])
	



	writeFile(ret5, back_to_words)

	


def back_to_words(index, dict1):
	return dict1[index]


def printOut(arg1, arg2, dict1):
	# Sort the frequent item_set based on their frequency and print in the descending order

	for item_set, support in reversed(sorted(arg1, key=lambda (item_set, support): support)):
		word = []
		for item in item_set:
			tmp = dict1[item]
			word.append(tmp)
		print "%d   %s" % (support, str(word).strip('[]'))






if __name__ == "__main__":

	optparser = OptionParser()
	optparser.add_option('-f', '--inputFile',
						 dest = 'input',
						 help = 'filename containing txt',
						 default = None)
	optparser.add_option('-s', '--minSupport',
						 dest = 'minS',
						 help = 'minimum support value',
						 default = 0.01,
						 type='float')
	optparser.add_option('-c', '--minConfidence',
						 dest = 'minC',
						 help = 'minimum confidence value',
						 default = 0.5,
						 type = 'float')

	(options, args) = optparser.parse_args()

	inFile = None
	if options.input is None:
			inFile = sys.stdin
	elif options.input is not None:
			inFile = options.input
			minSupport = options.minS
			minConfidence = options.minC
			Apriori(inFile, minSupport, minConfidence)
	else:
			print 'No dataset filename specified, system with exit\n'
			sys.exit('System will exit')













