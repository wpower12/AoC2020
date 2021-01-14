FN = '../inputs/05_boardingpasses.txt'
with open(FN, 'r') as f:
	lines = f.readlines()

def getSeatID(l):
	l = l[:10]
	l = l.replace('F', '0').replace('B', '1')
	l = l.replace('L', '0').replace('R', '1')
	row = int(l[:7], 2)
	col = int(l[-3:], 2)
	return row*8+col


seat_ids = []
for line in lines:
	seat_ids.append(getSeatID(line))

seat_ids = sorted(seat_ids)

for i in range(len(seat_ids)):
	if seat_ids[i]+1 != seat_ids[i+1]:
		print(seat_ids[i]+1)
		break
