FN = '../inputs/06_answers.txt'

with open(FN, 'r') as f:
	count = 0
	curr_set = set('')
	for line in f.readlines():
		if line == '\n': # Empty line
			count   += len(curr_set)
			curr_set = set('')
		else:
			curr_set = curr_set | set(line[:-1]) # Yay set ops!

	# THE LAST LINE. OMG.
	count += len(curr_set)

print(count)
