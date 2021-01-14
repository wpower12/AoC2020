FN = "../inputs/02_passwords.txt"

def parsePWLine(l):
	raw_split = l.split(' ')
	pw_char = raw_split[1][0] 
	pw_str  = raw_split[2]

	num_split = raw_split[0].split('-')
	char_min = int(num_split[0])
	char_max = int(num_split[1])
	return(char_min, char_max, pw_char, pw_str)

values = []
with open(FN, 'r') as f:
	lines = f.readlines()
	for line in lines:
		values.append(parsePWLine(line))

def validPW(v):
	c_min, c_max, c, pw_str = v
	c_count = pw_str.count(c)
	return c_count >= c_min and c_count <= c_max 

valid_pw_count = 0
for val in values:
	if validPW(val): valid_pw_count += 1

print(valid_pw_count)
