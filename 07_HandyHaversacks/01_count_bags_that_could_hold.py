FN = '../inputs/07_bagrules.txt'

adj_list = {} # Adjacency list for a graph of bag rules. Key is the node name. 

# Going to make the graph point the other direction, so from if bag A can contain bag B,
# there is an edge from B to A. This is so I can start the search at shinygold and go 
# backwards to all reachable bags. 

with open(FN, 'r') as f:
	lines = f.readlines()

	for line in lines:
		tokens = line.split(" ")

		node_to = tokens[0]+tokens[1]

		if node_to not in adj_list:
			adj_list[node_to] = []

		num_to = int((len(tokens)-4)/4)
		# if num_to is less than 1, 'node_from' is a sink, and this wont run.
		for i in range(num_to):
			node_from = tokens[5+i*4]+tokens[6+i*4]

			if node_from not in adj_list:
				adj_list[node_from] = []

			if node_to not in adj_list[node_from]:
				adj_list[node_from].append(node_to)

node_set = set(adj_list.keys())

seen = {}
for node in node_set:
	seen[node] = False

queue = []
queue.append('shinygold')
count = 0

while len(queue) > 0:
	# visit node - increment counter
	n = queue.pop()
	seen[n] = True
	count += 1
	for neighbor in adj_list[n]:
		if not seen[neighbor]:
			queue.append(neighbor)
			seen[neighbor] = True

print(len(node_set))
print(count-1)