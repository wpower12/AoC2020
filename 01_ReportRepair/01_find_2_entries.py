FN = "../inputs/01_entries.txt"
TARGET = 2020

values = []

with open(FN, 'r') as f:
	lines = f.readlines()
	for line in lines:
		values.append(int(line))

values = sorted(values)

res = []

for v in values:
	try:
		i = values.index(TARGET-v)
		print(values.index(TARGET-v))
		res = [v, TARGET-v]
	except:
		pass

print(res[0]*res[1])