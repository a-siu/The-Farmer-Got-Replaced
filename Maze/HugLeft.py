def solve():
	# artificially hugging the left wall
	facing = [North, West, South, East]
	i = 0
	while get_entity_type() == Entities.Hedge:
		if move(facing[(i + 1) % 4]):
			i = i + 1
		elif move(facing[i % 4]):
			continue
		elif move(facing[(i - 1) % 4]):
			i = i - 1
		else:
			i = i + 2
	harvest()

def make_maze():
	if get_entity_type() != Entities.Hedge:
		harvest()
		plant(Entities.Bush)
		while get_entity_type() == Entities.Bush:
			fertilize()

# demo with benchmark
op1 = get_op_count()
t1 = get_time()
for i in range(10):
	make_maze()
	solve()
print('Time: ', get_time() - t1)
print('Operation: ', get_op_count() - op1)
	