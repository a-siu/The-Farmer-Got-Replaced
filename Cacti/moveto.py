def moveto(x1=0, y1=0, push=False):
	dx = x1 % get_world_size() - get_pos_x()
	dy = y1 % get_world_size() - get_pos_y()
	if not push:
		dx = dx % get_world_size()
		dy = dy % get_world_size()
	
		if dx > get_world_size()//2:
			dx = dx - get_world_size()

		if dy > get_world_size()//2:
			dy = dy - get_world_size()
	if dx:
		unit_dx = dx/abs(dx)
		dir_x = {1:East, -1:West}[unit_dx]
	if dy:
		unit_dy = dy/abs(dy)
		dir_y = {1: North, -1: South}[unit_dy]
	if abs(dx) > abs(dy):
		for i in range(abs(dx)):
			if push:
				swap(dir_x)
			move(dir_x)
		for i in range(abs(dy)):
			if push:
				swap(dir_y)
			move(dir_y)
	else:
		for i in range(abs(dy)):
			if push:
				swap(dir_y)
			move(dir_y)
		for i in range(abs(dx)):
			if push:
				swap(dir_x)
			move(dir_x)

def moveto2(num=0, push=False):
	moveto(num // get_world_size(), num % get_world_size(), push)

def walk(dir, steps):
	pass
	
def carry(dir, steps):
	pass
	