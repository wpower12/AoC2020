FN = "../inputs/02_passwords.txt"

def parsePWLine(l):
	raw_split = l.split(' ')
	pw_char = raw_split[1][0] 
	pw_str  = raw_split[2]

	num_split = raw_split[0].split('-')
	char_p1 = int(num_split[0])
	char_p2 = int(num_split[1])
	return(char_p1, char_p2, pw_char, pw_str)

values = []
with open(FN, 'r') as f:
	lines = f.readlines()
	for line in lines:
		values.append(parsePWLine(line))

def validPW(v):
	c_p1, c_p2, c, pw_str = v
	v_p1 = pw_str[c_p1-1]
	v_p2 = pw_str[c_p2-1]

	if v_p1 == c and v_p2 == c: return False
	if v_p1 == c: return True
	if v_p2 == c: return True
	return False

valid_pw_count = 0
for val in values:
	if validPW(val): valid_pw_count += 1

print(valid_pw_count)
