FN = '../inputs/04_passports.txt'

REQUIRED = ['byr', 'iyr', 'eyr', 'hgt',
            'hcl', 'ecl', 'pid']

with open(FN, 'r') as f:
	lines = f.readlines()

passports = []

current_pp = []
for line in lines:
	if len(line) == 1:	# Is it just a single \n?
		passports.append(current_pp)
		current_pp = []
	else:
		pairs = line[:-1].split(' ')
		for pair in pairs:
			current_pp.append(pair.split(':')[0])
passports.append(current_pp)

def validPP(pp):
	keys  = set(pp) 
	for req in REQUIRED:
		if req not in keys:
			return False
	return True

count_valid_pp = 0
for pp in passports:
	if validPP(pp): count_valid_pp += 1

print(count_valid_pp)