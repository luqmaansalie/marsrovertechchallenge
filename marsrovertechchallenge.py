# marsrovertechchallenge
# https://code.google.com/archive/p/marsrovertechchallenge/

# assumptions
# the plateau is a sphere
# rovers cannot be placed where a rover currently is
# rovers cannot move into one another

moves = []
plateau = []

plateauX = 0
plateauY = 0

r = 0
d = ""
x = 0
y = 0

abort_mission = False
directions = ["n", "w", "s", "e"]

def rotate(direction, rotation):
	index = directions.index(direction.lower())
	index = index + 1 if rotation.lower() == "l" else index - 1
	index = 0 if index > 3 else (3 if index < 0 else index)
	
	return directions[index]

def print_move(m):
	if show_every_move:
		print(m + " --------------------------------------")
		for a in plateau:
			print(a)

def init_plateau():
	global abort_mission
	global plateau
	global plateauY
	global plateauX

	try:
		input_text = "Plateau dimentions (xdimention ydimention separated by a space) "
		l = input(input_text)
		if len(l) == 0:
			abort_mission = True
		else:
			plateauX = int(l.split(" ")[0])
			plateauY = int(l.split(" ")[1])
			for p in range (plateauX):
				plateau.append(["    "] * plateauY)
	
	except:
		init_plateau()

print("Press enter to exit")
input_text = "Show every move of each rover? (y/n) "
l = input(input_text).lower()
if len(l) == 0:
	abort_mission = True

if not abort_mission:
	show_every_move = True if l == "y" else False
	init_plateau()

if not abort_mission:
	r += 1
	input_text = "R" + str(r) + " details (xposition yposition n/w/s/e): "
	i = 0
	while not abort_mission:
		l = input(input_text)
		if len(l) == 0:
			break

		if i%2 == 0:
			try:
				rover = l.split(" ")

				d = rover[2].lower()
				x = int(rover[0])-1
				y = int(rover[1])-1

				directions.index(d)
				
				if plateau[x][y] != "    ":
					print("A rover is already located there")
					continue

				plateau[x][y] = "R" + str(r) + " " + d
				print_move(" ")
				input_text = "R" + str(r) + " moves (l/r/m): "
				i = 1
			except:
				print("Please place the rover on Mars and point it in a cardinal direction (n/w/s/e)")
		else:
			moves = list(l.lower())

			for m in moves:
				if m == "m":
					xtemp = x
					ytemp = y

					if d == "e":
						x = x+1 if x+1 < plateauX else 0
					elif d == "w":
						x = x-1 if x-1 > -1 else  plateauX-1
					elif d == "n":
						y = y+1 if y+1 < plateauY else 0
					elif d == "s":
						y = y-1 if y-1 > -1 else plateauY-1

					if plateau[x][y] == "    ":
						plateau[xtemp][ytemp] = "    "
					else:
						x = xtemp
						y = ytemp					
				else:
					d = rotate(d, m)
				
				plateau[x][y] = "R" + str(r) + " " + d
				print_move(m)
			r += 1
			input_text = "R" + str(r) + " details (xposition yposition n/w/s/e): "
			i = 0

if show_every_move:
	print("========================================")
	for a in plateau:
		print(a)

for row in range(plateauX):
	for col in range(plateauY):
		if plateau[row][col] != "    ":
			print(str(row+1) + " " + str(col+1) +" " + plateau[row][col].split(" ")[1])
