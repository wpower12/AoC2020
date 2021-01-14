# import copy

FN = "../inputs/11_seating.txt"

# with open(FN, 'r') as f:
# 	lines      = f.readlines()
# 	lines      = [list(x) for x in lines] # stripping newlines
# 	lines_buff = f.readlines()
# 	lines_buff = [list(x) for x in lines]

# for l in range(len(lines)):
# 	lines[l].pop()
# 	lines_buff[l].pop()

# # print(lines)

# while True:
# 	for i in range(len(lines[0])):
# 		for j in range(len(lines)):

# 			num_occupied = 0
# 			for di in [-1, 0, 1]:
# 				for dj in [-1, 0, 1]:
# 					if (di == 0 and dj == 0):
# 						pass
# 					elif ((di+i) > 0 and (di+i < len(lines[0])) and
# 						  (dj+j) > 0 and (dj+j < len(lines))):
# 						if lines[dj+j][di+i] == '#': num_occupied += 1 


# 			if   lines[j][i] == 'L' and num_occupied == 0:
# 				lines_buff[j][i] = '#'
# 			elif lines[j][i] == '#' and num_occupied >= 4:
# 				lines_buff[j][i] = 'L'
# 			else:
# 				lines_buff[j][i] = lines[j][i]

# 	the_same = True
# 	for l in range(len(lines)):
# 		for m in range(len(lines[0])):
# 			the_same = the_same and (lines[l][m] == lines_buff[l][m])

# 	lines = copy.deepcopy(lines_buff)
# 	if the_same: break


# count = 0
# for l in range(len(lines)):
# 	for m in range(len(lines[0])):
# 		if lines_buff[l][m] == '#': count += 1

# print(count)

with open(FN, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]
    lines = [list(line) for line in lines]

rows, cols = len(lines), len(lines[0])
deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def count_occupied(r, c, grid):
    count=0
    for i,j in deltas:
        xi,xj=r+i,c+j
        if 0<=xi<rows and 0<=xj<cols and grid[xi][xj]=='#':
            count+=1
    return count


def check_occupied(lines, thresh = 4):
    while True:
        valid = True
        temp_grid=[r.copy() for r in lines]
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied(i, j, temp_grid)
                if c=='L' and count==0:
                    lines[i][j]='#'
                elif c=='#' and count>=thresh:
                    lines[i][j]='L'
                valid&=(r[j]==lines[i][j])
        if valid:
            break
    ans=0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j]=='#':
                ans+=1
    print(f"There are {ans} valid seats.")
check_occupied(lines)
