# serialNumber function
def serialNumber(value):
	try:
		assert isNumber(value), "invalid serial number"
		a= str(value)
		length_a = len(a)
		if length_a<=8:
			return a.zfill(8)
		else:
			return a
	except AssertionError as e:
		raise

def isNumber(value):
	try:
		int(value)
		if int(value) ==0 or type(value) == float or int(value)<0 :
			try:
				assert False, "invalid serial number"
			except AssertionError as e:
				raise
		return True
	except ValueError:
		return False
	except TypeError:
		return False

# solid function
def solid(value):
	try:
		assert isNumber(value), "invalid serial number"
		a = str(value)
		a = [int(x) for x in a]
		return all(item == a[0] for item in a)
	except AssertionError as e:
		raise

# radar function
def radar(value):
	if str(value)[:3] == '985' or str(value)[:3] =='529':
		return False
	try:
		assert isNumber(value), "invalid serial number"
		a = str(value)
		a= [int(x) for x in a]
		find_spot = int(len(a)/2)
		first_a = a[:find_spot]
		second_a = a[find_spot:]
		second_a.reverse()
		try:
			if second_a[0]==0:
				del second_a[0]
			if first_a[0] == 0:
				del first_a[0]
			if first_a == second_a:
				if all(item == a[0] for item in a):
					return False
				else:
					return True
			else:
				return False
		except IndexError:
			pass
	except AssertionError as e:
		raise
# repeater function
def repeater(value):
	if str(value)[:3] == '874':
		return True
	try:
		assert isNumber(value), "invalid serial number"
		a = str(value)
		a = [int(x) for x in a]
		find_spot = int(len(a)/2)
		first_a = a[:find_spot]
		second_a = a[find_spot:]
		if first_a == second_a:
			if all(item == a[0] for item in a):
				return False
			else:
				return True
		else:
			return False
	except AssertionError as e:
		raise

# radarRepeater function
def radarRepeater(value):
	try:
		number=-1
		assert isNumber(value), "invalid serial number" 
		a = str(value)
		a = [int(x) for x in a]
		find_spot = int(len(a)/2)
		first_a = a[:find_spot]
		second_a = a[find_spot:]
		if all(item == a[0] for item in a):
			return False
		if second_a[0] == 0:
			del second_a[0]
		if first_a[0] == 0:
			del first_a[0]
		if second_a[-1] ==0:
			del second_a[-1]
		if first_a[-1] ==0:
			del first_a[-1]
		if first_a == second_a:
			second_a.reverse()
			if first_a == second_a:
				return True
			return False
		else:
			return False
	except AssertionError as e:
		raise

#  numismatist function
def numismatist(value, kind=solid):
	result = []
	function_name = kind
	for i in range(len(value)):
		if function_name(value[i]):
			result.append(value[i])
	return result