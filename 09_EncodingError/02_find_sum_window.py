FN = '../inputs/09_xmas.txt'
TARGET = 27911108

with open(FN, 'r') as f:
	lines = f.readlines()

lines = [int(x) for x in lines]
found = False
for start in range(0, len(lines)):
	for end in range(1, len(lines)):
		val = sum(lines[start:end])
		
		if val == TARGET:
			found = True
			break
			
		# speed things up a lil. 
		if val > TARGET:
			break

	if found: break

window = sorted(lines[start:end])
print(window[0]+window[-1])
