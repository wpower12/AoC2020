FN = "../inputs/10_adapters.txt"

with open(FN, 'r') as f:
	lines = f.readlines()
	lines = [int(x) for x in lines]

lines = sorted(lines)
# lines.append(lines[:-1]+3)

count_1 = 0
count_3 = 0

for i in range(len(lines)-1):
	this_val = lines[i]
	next_val = lines[i+1]

	if next_val-this_val == 1: count_1 += 1
	if next_val-this_val == 3: count_3 += 1

# accounting for the outlet
if lines[0] == 1: count_1 += 1
if lines[0] == 3: count_3 += 1

print(count_1*(count_3+1)) # +1 for the bags adapter