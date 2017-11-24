def crossSection(layer, direct):
	if int(len(direct)) %layer !=0 or len(direct)/2/layer != int(len(direct)/2/layer):
		try:
			assert False, "invalid cross section"
		except AssertionError as e:
			raise
	entire_result = []
	result = []
	number=-2
	for j in range(layer):
		for i in range(int(len(direct)/2/layer)):
			number +=2
			result.append(direct[number:number+2])
		entire_result.append(result)
		result=[]
	return entire_result

def depth(value):
	