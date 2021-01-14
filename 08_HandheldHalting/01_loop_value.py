FN = '../inputs/08_instructions.txt'
SEEN = 2

program = []
with open(FN, 'r') as f:
	lines = f.readlines()
	for line in lines:
		line_raw = line.split(" ")
		instr = line_raw[0]
		value = int(line_raw[1][:-1])
		# I'll track a 'seen' flag in the third value.
		program.append([instr, value, False])

acc_val = 0
pc = 0

while not program[pc][SEEN]:
	instr, value, _ = program[pc]
	program[pc][SEEN] = True

	if instr == "acc":
		acc_val += value
		pc += 1

	if instr == "jmp":
		pc += value

	if instr == "nop":
		pc += 1


print(acc_val)