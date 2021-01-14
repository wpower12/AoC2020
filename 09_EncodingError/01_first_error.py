FN = '../inputs/09_xmas.txt'
WIDTH = 25 # Size of the preamble.

with open(FN, 'r') as f:
	lines = f.readlines()

window = []
# Fill the sliding window with the preamble.
for i in range(WIDTH+1):
	window.append(int(lines[i]))

for i in range(WIDTH, len(lines)):
	# check condition
	target = int(lines[i])
	seen = False
	for a in window:
		if abs(target-a) in window:
			seen = True
	if not seen:
		print(target)
		break

	# update window
	window.pop(0)	# Need to pop the 'first' item, default is last. 
	window.append(target)
