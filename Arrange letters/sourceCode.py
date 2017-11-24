bag = 'IAMDIETINGIEATQUINCEJELLYLOTS000000UNDMAIEHFIVBEIFOSJFON_RJHR_EWBVUR'


def fill(value):
	value = list(value)
	wordcount = {}
	for word in value:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1
	return wordcount

def description(value):
	clusters = {}
	try:
		values = set(value.values())
		keys = value.keys()
	except AttributeError:
		values = set(value)
		keys = range(len(value))
	for i in values:
		clusters[i] = set(filter(lambda v: value[v] == i, keys))
	return clusters

def remove(v1, v2):
	number = -1
	result = ''
	v2_value = list(v2.values())
	v2_key = list(v2.keys())
	for i in v2_value:
		number +=1
		result += v2_value[number] * v2_key[number]
	number = -1
	result = list(result)
	for item in v1:
		if item in result:
			del(result[result.index(item)])
		else:
			try:
				assert False, "not all letters are in the bag"
			except AssertionError as e:
				raise
	for letter in v1:
		v2[letter] = v2.setdefault(letter, 0) - 1
		if v2[letter] ==0:
			del v2[letter]