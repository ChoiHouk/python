def triangle(value):
	if type(value) != int:
		try:
			assert False, "invalid number of rows"
		except AssertionError as e:
			raise
	else:
		if value <0:
			try:
				assert False, "invalid number of rows"
			except AssertionError as e:
				raise
	height = value
	triangle = []
	row = []
	prev_row = []
	for i in range(0, height + 1):
		row = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] + prev_row[j] or 1 for j in range(0, i)]
		prev_row = row
		triangle += [row]
	return triangle[1:]

def hexagon(row, col):
	if col -2<0 or row-2<0:
		try:
			assert False, "invalid internal position"
		except AssertionError as e:
			raise
	try:
		assert Indexrange(row, col), "invalid internal position"
	except AssertionError as e:
		raise
	entry = triangle(row+1)
	first = entry[row-2][col-2]
	second = entry[row-2][col-1]
	third = entry[row-1][col]
	fourth = entry[row][col]
	fith = entry[row][col-1]
	sixth = entry[row-1][col-2]
	return [first, second, third, fourth, fith, sixth]

def Indexrange(row, col):
	try:
		entry = triangle(row+1)
		first = entry[row-2][col-2]
		second = entry[row-2][col-1]
		third = entry[row-1][col]
		fourth = entry[row][col]
		fith = entry[row][col-1]
		sixth = entry[row-1][col-2]
	except IndexError:
		return False
	return True

def square(row, col):
	result = ''
	if col -2<0 or row-2<0:
		try:
			assert False, "invalid internal position"
		except AssertionError as e:
			raise
	try:
		assert Indexrange(row, col), "invalid internal position"
	except AssertionError as e:
		raise
	entry = triangle(row+1)
	first = entry[row-2][col-2]
	second = entry[row-2][col-1]
	third = entry[row-1][col]
	fourth = entry[row][col]
	fifth = entry[row][col-1]
	sixth = entry[row-1][col-2]
	multiply = first*second*third*fourth * fith * sixth
	root_multi = int(multiply**0.5)
	result = str(first)+' x '+str(second)+' x '+str(third)+' x '+str(fourth)+' x '+str(fifth)+' x '+str(sixth)+' = '+ str(multiply)+' = '+str(root_multi)+' x '+str(root_multi)
	return result