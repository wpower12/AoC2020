FN = "../inputs/01_entries.txt"
TARGET = 2020

values = []

with open(FN, 'r') as f:
	lines = f.readlines()
	for line in lines:
		values.append(int(line))

values = sorted(values)

res = []

for v1 in values:
	for v2 in values:
		try:
			i = values.index(TARGET-(v1+v2))
			# print(values.index(TARGET-v))
			res = [v1, v2, TARGET-(v1+v2)]
		except:
			pass

print(res[0]*res[1]*res[2])