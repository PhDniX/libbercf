input_file = "morocco"
#input_file = raw_input("Insert filename:")

with open(input_file + ".txt", "r") as data:
	lines = []
	linesdict = {}
	for line in data:
		line = line.strip().split(",")
		linecut = line[1]
		lines.append(linecut)
		#Make a dictionary 'linesdict' of the input file Key = place, value = text
		linesdict[line[0]] = line[1]

#Get longest substring of two strings.
#http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python
def longest_substring(s1, s2):
	m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
	longest, x_longest = 0, 0
	for x in xrange(1, 1 + len(s1)):
		for y in xrange(1, 1 + len(s2)):
			if s1[x - 1] == s2[y - 1]:
				m[x][y] = m[x - 1][y - 1] + 1
				if m[x][y] > longest:
					longest = m[x][y]
					x_longest = x
			else:
				m[x][y] = 0
	return s1[x_longest - longest: x_longest]

#Compare each string in the file with each other string.
def iter_strings(data):
	result = []
	x = ""
	for index1, item1 in enumerate(data):
		for index2, item2 in enumerate(data):
			if index1 != index2:
				x = longest_substring(data[index1], data[index2])
				if len(x) >= 3:
					result.append(x)
	return result

set_output = set(iter_strings(lines))
list_output = list(set_output)
ordered_list = list_output.sort(lambda y,x: cmp(len(x), len(y))) #Why does this work while the write function does not call ordered_list?

#print linesdict

#print list_output

#Create a dictionary that shows whether a substring occurs in an inscription
#Right now it does not check if a certain string occurs in multiple inscriptions.
def placedict(dct, string):
	result = {}
	for value in dct:
		for line in string:
			if line in dct[value]:
				result.update({line:value})
	return result

final_dict = placedict(linesdict, list_output)

f = open("outputdict.txt", "w")

for key in final_dict.keys():
	f.write(str(key) + ":" + str(final_dict[key] + "\n"))

f.close()