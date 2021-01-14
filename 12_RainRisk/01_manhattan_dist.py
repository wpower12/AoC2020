FN = "../inputs/12_movements.txt"

with open(FN, 'r') as f:
	movements = [[x[0], int(x[1:])] for x in f.readlines()]

x, y    = 0, 0 # East, North directions
f       = 0    # f++ = CCW, f-- = CW
facings = ['E', 'N', 'W', 'S']

for d, v in movements:
	# Translation moves.
	if d == 'N':
		y += v
	if d == 'S':
		y -= v
	if d == 'E':
		x += v
	if d == 'W':
		x -= v

	# Rotations. 
	if d == 'L':
		# rotate CCW
		f += (int(v / 90) % 4)
		if f > 3: f = 0
	if d == 'R':
		# rotate CW
		f -= (int(v / 90) % 4)
		if f < 0: f = 3

	# F/B Moves
	if d == 'F':
		if facings[f] == 'E':
			x += v
		if facings[f] == 'W':
			x -= v
		if facings[f] == 'N':
			y += v
		if facings[f] == 'S':
			y -= v
		
print(abs(x)+abs(y))
