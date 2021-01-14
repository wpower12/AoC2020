import re

FN = '../inputs/04_passports.txt'

REQUIRED   = ['byr', 'iyr', 'eyr', 'hgt',
              'hcl', 'ecl', 'pid']
EYE_COLORS = ['amb', 'blu', 'brn', 'gry',
			  'grn', 'hzl', 'oth']

with open(FN, 'r') as f:
	lines = f.readlines()

passports = []

current_pp = {}
for line in lines:
	if len(line) == 1:	# Is it just a single \n?
		passports.append(current_pp)
		current_pp = {}
	else:
		pairs = line[:-1].split(' ')
		for pair in pairs:
			key, val = pair.split(':')
			current_pp[key] = val
			
passports.append(current_pp)

def validPP(pp):
	for req in REQUIRED:
		if req not in pp:
			return False
		
		if req == 'byr':
			year = int(pp[req])
			if year < 1920 or year > 2002: 
				return False
		if req == 'iyr':
			year = int(pp[req])
			if year < 2010 or year > 2020: 
				return False
		if req == 'eyr':
			year = int(pp[req])
			if year < 2020 or year > 2030: 
				return False
		if req == 'hgt':
			hgt_str = pp[req]
			unit  = hgt_str[-2:]
			if unit == "in" or unit == "cm":
				value = int(hgt_str[:-2])
				if unit == "cm" and (value < 150 or value > 193):
					return False
				if unit == "in" and (value < 59 or value > 76):
					return False
			else:
				return False
		if req == 'hcl':
			hcl_str = pp[req]
			# if hcl_str[0] != '#': return False
			if re.fullmatch('#[0-9a-f]{6}', hcl_str) == None:
				return False
		if req == 'ecl':
			if pp[req] not in EYE_COLORS: 
				return False
		if req == 'pid':
			if re.fullmatch('[0-9]{9}', pp[req]) == None: 
				return False		
	return True


count_valid_pp = 0
for pp in passports:
	if validPP(pp): 
		count_valid_pp += 1

print(count_valid_pp)
