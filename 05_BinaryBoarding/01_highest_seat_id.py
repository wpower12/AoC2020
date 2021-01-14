# Taking the hint and treating these as representations of binary values. 

FN = '../inputs/05_boardingpasses.txt'

with open(FN, 'r') as f:
	lines = f.readlines()

def getSeatID(l):
	l = l[:10]
	l = l.replace('F', '0').replace('B', '1')
	l = l.replace('L', '0').replace('R', '1')
	row = int(l[:7],  2)
	col = int(l[-3:], 2)
	return row*8+col


highest_id = 0
for line in lines:
	v = getSeatID(line)
	if v > highest_id:
		highest_id = v

print(highest_id)
