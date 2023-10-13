import random,sys
import pygame as p

SIZE = 20 #---size of col or row in map---#
MAX_TUNNELS = 100 #---max amount of rooms---#
MAX_LENGTH = 5 #---max amount of tunnels in a row---#
CELL_SIZE = 50
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

WIN = p.display.set_mode((CELL_SIZE*SIZE,CELL_SIZE*SIZE))

def set_empty_map():
	new_map = [[0 for x in range(SIZE)] for i in range(SIZE)]
	return new_map

def make_map(current_map):
	tunnels_used = 0
	random_point = [random.randint(0,SIZE-1),random.randint(0,SIZE-1)]
	current_pos = random_point
	current_map[random_point[0]][random_point[1]] = 1
	prev_dir = [0,0]
	while tunnels_used + 1 < MAX_TUNNELS:
		direction = get_dir(prev_dir)
		tunnel_length = random.randint(1,MAX_LENGTH)
		for i in range(tunnel_length):
			if (current_pos[0] + direction[0] >= SIZE or current_pos[0] + direction[0] <= 0 ) or (current_pos[1] + direction[1] >= SIZE or current_pos[1] + direction[1] <= 0):
				pass
			else:
				current_pos[0],current_pos[1] = current_pos[0] + direction[0], current_pos[1] + direction[1]
				current_map[current_pos[0]][current_pos[1]] = 1
				tunnels_used += 1
				prev_dir = direction

	return current_map


def get_dir(prev_dir):
	directions = [[0,1],[0,-1],[-1,0],[1,0]]
	rand_dir = random.choice(directions)
	while (rand_dir[0] == prev_dir[0] and rand_dir[1] == prev_dir[1]) or (rand_dir[0] == -prev_dir[0] and rand_dir[1] == -prev_dir[1]):
		rand_dir = random.choice(directions)

	return rand_dir



def output_map(current_map):
	for col in range(SIZE):
		for row in range(SIZE):
			x = row*CELL_SIZE
			y = col*CELL_SIZE
			new_rect = p.Rect(x,y,CELL_SIZE,CELL_SIZE)
			if current_map[col][row] == 1:
				colour = RED
			else:
				colour = WHITE
			p.draw.rect(WIN,colour,new_rect)

def update(current_map):
	WIN.fill(BLACK)
	output_map(current_map)
	p.display.update()

def main():
	current_map = make_map(set_empty_map())
	while True:
		for event in p.event.get():
			if event.type == p.QUIT:
				p.quit()
				sys.exit()
			elif event.type == p.MOUSEBUTTONDOWN:
				current_map = make_map(set_empty_map())

		update(current_map)

if __name__ == "__main__":
	main()