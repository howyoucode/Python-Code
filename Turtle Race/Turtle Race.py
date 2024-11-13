import turtle
import random
import time

WIDTH = 1000
HEIGHT = 700
COLORS = ['alice blue', 'antique white', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanched almond', 'blue',
 'blue violet', 'brown', 'burly wood', 'cadet blue', 'chartreuse', 'chocolate', 'coral', 'cornflower blue', 
 'cornsilk', 'crimson', 'cyan', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark green', 
 'dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 
 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark turquoise', 'dark violet', 'deep pink', 
 'deep sky blue', 'dim gray', 'dodger blue', 'firebrick', 'floral white', 'forest green', 'fuchsia', 
 'gainsboro', 'ghost white', 'gold', 'goldenrod', 'gray', 'green', 'green yellow', 'honeydew', 'hot pink', 
 'indian red', 'indigo', 'ivory', 'khaki', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 
 'light blue', 'light coral', 'light cyan', 'light goldenrod yellow', 'light gray', 'light green', 
 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate gray', 'light steel blue', 
 'light yellow', 'lime', 'lime green', 'linen', 'magenta', 'maroon', 'medium aquamarine', 'medium blue', 
 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 
 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'moccasin', 
 'navajo white', 'navy', 'old lace', 'olive', 'olive drab', 'orange', 'orange red', 'orchid', 'pale goldenrod', 
 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'plum', 
 'powder blue', 'purple', 'red', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'sandy brown', 
 'sea green', 'seashell', 'sienna', 'silver', 'sky blue', 'slate blue', 'slate gray', 'snow', 'spring green', 
 'steel blue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'white smoke', 
 'yellow', 'yellow green']

def get_num_of_racers():
    while True:
        racers = input("Enter how many racers do you want to add to race (2-7): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Please enter a numeric...')
            continue
        if 2 <= racers <= 7:
            return racers
        else:
            print("Enter number in range!")

def get_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("How You Turtle Racing")

def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles


racers = get_num_of_racers()
get_screen()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
