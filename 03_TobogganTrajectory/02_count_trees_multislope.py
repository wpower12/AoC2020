FN = '../inputs/03_trees.txt'
SLOPES = [[1, 1],
		  [3, 1],
		  [5, 1],
		  [7, 1],
		  [1, 2]]

with open(FN, 'r') as f:
	lines = f.readlines()

# Should address like treescape[y][x]
treescape = []
for line in lines:
	treescape.append(line[:-1])
width = len(treescape[0])
goal  = len(treescape)

res = 1

for dx, dy in SLOPES:
	x, y  = 0, 0
	count = 0
	while y+dy < goal:
		x = (dx+x) % width
		y += dy

		if treescape[y][x] == '#': count += 1

	res *= count

print(res)
