FN = '../inputs/08_instructions.txt'
SEEN = 2

def getProgram(FN):
	program = []
	with open(FN, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line_raw = line.split(" ")
			instr = line_raw[0]
			value = int(line_raw[1][:-1])
			# I'll track a 'seen' flag in the third value.
			program.append([instr, value, False])
	return program

found = False
to_flip_id = 0
program = getProgram(FN)

while to_flip_id < len(program):
	inst_to_flip = program[to_flip_id][0]

	if inst_to_flip in ["jmp", "nop"]:
		program = getProgram(FN)
		acc_val = 0
		pc = 0
		while not program[pc][SEEN]:
			instr, value, _   = program[pc]
			program[pc][SEEN] = True

			if pc == to_flip_id:
				if instr == "jmp": 
					instr = "nop"
				else: 
					instr = "jmp"

			if instr == "acc":
				acc_val += value
				pc += 1

			if instr == "jmp":
				pc += value

			if instr == "nop":
				pc += 1

			if pc == len(program)-1:
				print(acc_val)
				found = True
				break

	to_flip_id += 1
	if found: break
