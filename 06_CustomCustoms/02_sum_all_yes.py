FN = '../inputs/06_answers.txt'

with open(FN, 'r') as f:
	count = 0
	curr_sets = []
	for line in f.readlines():
		if line == '\n': # Empty line
			res_set = set('abcdefghijklmnopqrstuvwxyz')
			for s in curr_sets:
				res_set = res_set & s
			count += len(res_set)
			curr_sets = []
		else:
			curr_sets.append(set(line))

	# Processing the last line - oof. this bug took too long to find. 
	res_set = set('abcdefghijklmnopqrstuvwxyz')
	for s in curr_sets:
		res_set = res_set & s
	count += len(res_set)

print(count)
