# Source: Wikipedia of A* Algorithm
# Modified from pseudocode

		
def adjacentCoords(coords, dir):
	dirToOffset = {North: (0, 1), East: (1, 0), South: (0, -1), West: (-1, 0)}
	(offset_x, offset_y) = dirToOffset[dir]
	new_x, new_y = coords[0] + offset_x, coords[1] + offset_y
	
	return (new_x % get_world_size(), new_y % get_world_size())
	
def A_Star(start, goal, map):
	
	def func_h(goal, now={}):
		if not now:
			now = coords()
		return abs(goal[0] - now[0]) + abs(goal[1] - now[1])	
	
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    # openSet = {start}

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start
    # to n currently known.
    cameFrom = dict()

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = dict() # with default value of Infinity
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    # fScore = dict()
    # fScore[start] = func_h(goal)
    fScoreOpenSet = dict()
    fScoreOpenSet[func_h(goal)] = {start}

    while fScoreOpenSet:
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        minfScore = min(fScoreOpenSet)
        # current = minValue(openSet, fScore)
        minfScoreCoords = fScoreOpenSet[minfScore]
        for coord in minfScoreCoords: # This is a very bad way to get an element out of the set
            current = coord
            break
        # # # the node in openSet having the lowest fScore[] value
        if current == goal:
            return reconstruct_path(cameFrom, current)

        minfScoreCoords.remove(current)
        # openSet.remove(current)
        if not minfScoreCoords:
           fScoreOpenSet.pop(minfScore)
        availableDirections = map[current]
        for dir in availableDirections:
            neighbor = adjacentCoords(current, dir)
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + 1
            if tentative_gScore < get(neighbor, gScore, 9999):
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                tentative_fScore = tentative_gScore + func_h(goal)
                # fScore[neighbor] = tentative_fScore
                coordsSet = get(tentative_fScore, fScoreOpenSet, set())
                if neighbor not in coordsSet:
                    coordsSet.add(neighbor)      

   
    # Open set is empty but goal was never reached
    return 0

#demo
(map, location) = walkInThePark()
path = A_Star(coords(), location, map)
for i in range(1,len(path)):
	oneStep(path[i - 1], path[i])