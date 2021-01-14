FN = '../inputs/03_trees.txt'

DX = 3
DY = 1 # Even though its 'down' were going 'up' wrt the array

with open(FN, 'r') as f:
	lines = f.readlines()

# Should address like treescape[y][x]
treescape = []
for line in lines:
	treescape.append(line[:-1])
width = len(treescape[0])
goal  = len(treescape)
x, y  = 0, 0
count = 0

while y+DY < goal:
	x = (DX+x) % width
	y += DY

	if treescape[y][x] == '#': count += 1

print(count)
