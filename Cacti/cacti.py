def farm_cacti():
	for x in range(get_world_size()):
		moveto(x, 0)
		column = list()
		for y in range(get_world_size()):
			# does not destroy cactus but harvest other crops
			# and then plant
			safePlant(Entities.Cactus)
			column.append(measure())
			move(North)
		for i in range(get_world_size()):
			# find(list, value) - return index of value in list
			minTile = find(column, min(column))
			column.pop(minTile)
			if not minTile:
				continue
			# moveto(x, y, swaping, warping)
			# swaping: swap the plant when the drone moves
			# warping: allows warping at the edge
			
			# moveto executes the shortest path to the destination
			# with the constrain of warping allowed or disallowed
			moveto(x, minTile + i)
			
			# push the cactus without warping at the edge
			moveto(x, i, 1)  
	
	# Same for the other direction
	for y in range(get_world_size()):
		moveto(0, y)
		row = list()
		for x in range(get_world_size()):
			safePlant(Entities.Cactus)
			row.append(measure())
			move(East)
		for i in range(get_world_size()):
			minTile = find(row, min(row))
			row.pop(minTile)
			if not minTile: 
				continue
			moveto(minTile + i, y)
			moveto(i, y, 1)
	harvest()

# set_execution_speed(10)
while 1:
	farm_cacti()