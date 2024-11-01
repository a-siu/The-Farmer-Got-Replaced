def recordMove(dir, map, backstep=False):
	init_xy = (get_pos_x(), get_pos_y())
	if not move(dir):
		return False
	new_xy = (get_pos_x(), get_pos_y())
	init_xy_exploredDir = get(init_xy, map, set())
	if dir not in init_xy_exploredDir:
		init_xy_exploredDir.add(dir)
	new_xy_exploredDir = get(new_xy, map, set())
	if opposite(dir) not in new_xy_exploredDir:
		new_xy_exploredDir.add(opposite(dir))
	if backstep:
		move(opposite(dir))
	return True
	
def oneStep(current, next):
	dx = next[0] - current[0] 
	dy = next[1] - current[1]
	if dx:
		if dx > 0:
			return move(East)
		return move(West)
	if dy > 0:
		return move(North)
	return move(South)
	
def opposite(dir):
	oppDir = {North: South, South: North,
		East: West, West: East}
	return oppDir[dir]
	
def walkInThePark():
	# artificially hugging the left wall
	facing = [North, West, South, East]
	i = 0
	
	allNodes = dict()
	
	while len(allNodes) < get_world_size() ** 2: 
		if get_entity_type() == Entities.Treasure:
				treasureLocation = coords()
		if recordMove(facing[(i + 1) % 4], allNodes):
			i = i + 1
		elif recordMove(facing[i % 4], allNodes):
			continue
		elif recordMove(facing[(i - 1) % 4], allNodes):
			i = i - 1
		else:
			i = i + 2
	if get_entity_type() == Entities.Treasure:
		treasureLocation = coords()
		
	return (allNodes, treasureLocation)

# demo
map = walkInThePark()[0]
print(map[coords()])
for dir in allDir():
	print(map[adjCoords(coords(), dir)])