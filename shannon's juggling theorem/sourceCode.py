def missing_parameter(v1, v2):
	number = -1
	v1 = list(v1.keys())
	v2 = list(v2)
	if len(v1)+1 == len(v2):
		pass
	else:
		try:
			assert False, "invalid parameters"
		except AssertionError as e:
			raise
	for item in v1:
		number +=1
		if v1[number] not in v2:
			try:
				assert False, "invalid parameters"
			except AssertionError as e:
				raise
	number = -1
	for item in v2:
		number +=1
		if v2[number] not in v1:
			return v2[number]

def juggle(dic):
	solve = 0.0
	standard = 'FDVBH'
	add_value = missing_parameter(dic, standard)
	if add_value =='F':
		solve = round((dic['B']*(round(dic['V']+dic['D'], 3))/dic['H'])-dic['D'], 3)
	if add_value =='H':
		solve = round((dic['B']*(round(dic['V']+dic['D'], 2))/ round(dic['F']+dic['D'], 2)))
	if add_value =='D':
		solve = (dic['B']*dic['V'] - dic['H']*dic['F'])/(dic['H']-dic['B'])
	if add_value =='B':
		solve = round((dic['H']*(round(dic['F']+dic['D'], 2))/ round(dic['V']+dic['D'], 2)))
	if add_value =='V':
		solve = round((dic['H']*(round(dic['F']+dic['D'], 2))/dic['B'])-dic['D'], 2)
	dic[add_value] = solve
	for item in list(dic.keys()):
		dic[item] = float(dic[item])
	return dic
	
def juggler(F=0, D=0, V=0, B=0, H=0, **kwargs):
	if len(kwargs)>=1:
		try:
			assert False, "invalid parameters"
		except AssertionError as e:
			raise
	number= -1
	dic = {'F' :F, 'D':D, 'V':V, 'B':B, 'H':H}
	length_dic = dic
	index_list = []
	solve = 0.0
	standard = 'FDVBH'
	for i in length_dic:
		number+=1
		if list(dic.values())[number] == 0:
			index_list.append(number)
	for i in index_list:
		del dic[list(dic.keys())[i]]
	if len(dic) != 4:
		try:
			assert False, "invalid parameters"
		except AssertionError as e:
			raise
	dic = juggle(dic)
	return dic