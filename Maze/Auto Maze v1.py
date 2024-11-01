def auto_maze(times=300, benchmark=False):
	(map, goal) = walkInThePark() 
	for time in range(times):
		path = A_Star(coords(), goal, map)
		for i in range(1,len(path)):
			oneStep(path[i - 1], path[i])
			exploredDir = map[path[i]]
			if len(exploredDir) < 4:
				for dir in allDir():
					if dir in exploredDir:
						continue
					recordMove(dir, map, True)
		
		if time == times - 1:
			harvest()
			break
		goal = measure()
		while get_entity_type() == Entities.Treasure:
			fertilize()

# demo with benchmark
op1 = get_op_count()
t1 = get_time()
make_maze()
auto_maze(10)
print('Time: ', get_time() - t1)
print('Operation: ', get_op_count() - op1)