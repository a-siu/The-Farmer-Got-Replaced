def find(arr, value):
	for i in range(len(arr)):
		if arr[i] == value:
			return i
	return -1

def getSeed(crop):
	for key in get_cost(crop):
		return key

def measureNewCrop(tile, map, crop):
	safePlant(crop)
	if measure() in map:
		map[measure()].add(tile)
	else:
		map[measure()] = {tile}
	
def entityToItem(entity):
	mapping = {Entities.Bush: Items.Wood, Entities.Cactus: Items.Cactus, 
		Entities.Carrots: Items.Carrot, Entities.Dinosaur: Items.Bones, 
		Entities.Grass: Items.Hay, Entities.Pumpkin: Items.Pumpkin, 
		Entities.Sunflower: Items.Power, Entities.Treasure: Items.Gold, 
		Entities.Tree: Items.Wood}
	if entity in mapping:
		return mapping[entity]
	return None

def cropToMap(crop, xrange=get_world_size(), yrange=get_world_size()):
	map = {}
	for x in range(xrange):
		for y in range(yrange):
			moveto(x,y)
			if can_harvest() and get_entity_type() != crop:
				harvest()
			measureNewCrop(tile(), map, crop)
	return map

def safePlant(crop):
	if get_entity_type() == crop:
		return
	harvest()
	getStock(getSeed(crop))
	if not plant(crop):
		till()
		plant(crop)
		
def getStock(item, factor=0.01, minimum=0):
	if item == None:
		return True
	if num_items(item) > 5:
		return 1
	costMap = get_cost(item)
	numBuy = 0
	for key in costMap:
		if not numBuy:
			numBuy = num_items(key)*factor//(costMap[key])
		else:
			numBuy = min(num_items(key)*factor//(costMap[key]), numBuy)

	if numBuy < minimum:
		return trade(item, minimum)
	if not numBuy:
		return False
	return trade(item, numBuy)
	
	