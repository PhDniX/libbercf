input_file = raw_input("Insert filename:")

with open(input_file + ".txt", "r") as data:
	lines = []
	for line in data:
		line = line.strip()
		lines.append(line)

#http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python
#Get longest substring of two strings.
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
				if len(x) >= 2:
					result.append(x)
	return result

set_output = set(iter_strings(lines))
list_output = list(set_output)
ordered_list = list_output.sort(lambda y,x: cmp(len(x), len(y))) #Why does this work while the write function does not call ordered_list?

f = open("output.txt", "w")

for item in list_output:
    f.write(str(item) + "\n")

f.close()