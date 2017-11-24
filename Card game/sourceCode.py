import random
import itertools
SUITS = 'CDHS'
RANKS = '23456789XJQKA'
DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
list_deck = list(DECK)

def draw(drawn=[]):
	list_deck = [x for x in DECK if x not in drawn]
	return random.sample(list_deck, 1)[0]

def arrange(rows=5, cols=5):
	number = -1
	num = rows * cols
	matrix = []
	try:
		assert isTrue(rows, cols), "invalid grid"
		arrange_num = random.sample(list_deck,num)
		for i in range(rows):
			tmp = []
			for j in range(cols):
				number +=1
				tmp.append(arrange_num[number])
			matrix.append(tmp)
	except AssertionError as e:
		raise
	return matrix
	

def isTrue(rows, cols):
	num = rows * cols
	try:
		arrange_num = random.sample(list_deck,num)
		return True
	except ValueError:
		return False

def extend(grid=[]):
	number = -1
	subtract_value = list(itertools.chain(*grid))
	new_deck = [item for item in list_deck if item not in subtract_value]
	if len(new_deck) <=12:
		try:
			assert False, "invalid grid"
		except AssertionError as e:
			raise
	add_value = random.sample(new_deck, len(grid[:][0]))
	grid.append(add_value)
	new_deck = [item for item in new_deck if item not in add_value]
	add_value = random.sample(new_deck, len(grid))
	for j in grid:
		number +=1
		grid[:][number].append(add_value[number])



def select(grid=[]):
	import random
	end_rows = len(grid)
	end_cols = len(grid[:][0])
	first = random.randrange(0, end_rows)
	second = random.randrange(0, end_cols)
	return (first, second)