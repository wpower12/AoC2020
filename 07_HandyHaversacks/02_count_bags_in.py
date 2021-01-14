FN = '../inputs/07_bagrules.txt'

adj_list = {} # Adjacency list for a graph of bag rules. Key is the node name. 

with open(FN, 'r') as f:
	lines = f.readlines()

	for line in lines:
		tokens = line.split(" ")

		node_from = tokens[0]+tokens[1]

		if node_from not in adj_list:
			adj_list[node_from] = []

		num_to = int((len(tokens)-4)/4)
		# if num_to is less than 1, 'node_from' is a sink, and this wont run.
		for i in range(num_to):
			weight    = int(tokens[4+i*4])
			node_to   = tokens[5+i*4]+tokens[6+i*4]
			adj_list[node_from].append([node_to, weight])


def count_in(node):
	if len(adj_list[node]) == 0:
		return 1
	else:
		ret = 1 # We count this bag (node) here. 
		for n in adj_list[node]:
			neighbor, weight = n
			ret += weight*count_in(neighbor)
		return ret

print(count_in('shinygold')-1) # the -1 is to remove the count for the shinygold bag.
