#coding:utf-8

import tkinter
import random
import pickle
from tkinter import Frame, Label


#Création de la fênetre
app = tkinter.Tk()
app.geometry("653x710+10+10")
app.resizable(width=False, height=False)
app.title(2048)
#end

l_score = [0] * 2
l_grid = [0] * 16
l_copy = [0] * 16
l_score_copy = [0]

def update_score():
	with open("Highscore.data", "wb") as file_hs:
		put_score = pickle.Pickler(file_hs)
		put_score.dump(l_score[1])

try:
	with open("Highscore.data", "rb") as file_hs:
		get_score = pickle.Unpickler(file_hs)
		l_score[1] = get_score.load()
except:
	update_score

#entry_w = tkinter.Entry(app)
#mainframe
mainframe = Frame(app, bg="dimgray")
mainframe.pack(fill="both", expand = True)
#end

#Display
horizontal_frame = Frame(mainframe)

label_2048 = Label(horizontal_frame, text = "2048", padx = 40, pady = 0, font =("Arial", 54), bg = "yellow")
label_2048.grid(row = 0, rowspan = 4, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "nsew")

def display_score():
	
	label_score = Label(horizontal_frame, text = "Score", padx = 80, pady = 10, font = ("Arial", 24, 'bold'), bg = "gray")
	label_score.grid(row = 0, column = 3, padx = 0, pady = 0 , sticky = "nsew")
	label_score_nb = Label(horizontal_frame, text = l_score[0], padx = 0, pady = 0, font = ("Arial", 20, 'bold'), bg = "gray")
	label_score_nb.grid(row = 2, column = 3, padx = 0, pady = 0 , sticky = "nsew")

	label_highscore = Label(horizontal_frame, text = "Highscore", padx = 10, pady = 10, font = ("Arial", 24, 'bold'), bg = "gray")
	label_highscore.grid(row = 0, column = 4, padx = 0, pady = 0, sticky = "nsew")
	label_highscore_nb = Label(horizontal_frame, text = l_score[1], padx = 0, pady = 0, font = ("Arial", 20, 'bold'), bg = "gray")
	label_highscore_nb.grid(row = 2, column = 4, padx = 0, pady = 0, sticky = "nsew")

	horizontal_frame.grid_columnconfigure(0, weight = 1)
	horizontal_frame.grid_columnconfigure(1, weight = 1)
	horizontal_frame.grid_columnconfigure(2, weight = 1)
	horizontal_frame.grid_columnconfigure(3, weight = 1)
	horizontal_frame.pack(fill = "x")
display_score()
#end horizontal

#print_grid
grid_frame = Frame(mainframe, bg="dimgray")
def print_grid(i):

	for row in range(4):
		for column in range(4):
			if l_grid[i] == 0:
				label = Label(grid_frame, text = l_grid[i], bg = "gray", fg = "gray", padx = 68, pady = 55, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 2 or l_grid[i] == 4:
				label = Label(grid_frame, text = l_grid[i], bg = "gray", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 8:
				label = Label(grid_frame, text = l_grid[i], bg = "orange", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 16:
				label = Label(grid_frame, text = l_grid[i], bg = "orangered", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 32:
				label = Label(grid_frame, text = l_grid[i], bg = "lightcoral", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 64:
				label = Label(grid_frame, text = l_grid[i], bg = "red", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 128:
				label = Label(grid_frame, text = l_grid[i], bg = "gold", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 256:
				label = Label(grid_frame, text = l_grid[i], bg = "yellow", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 512:
				label = Label(grid_frame, text = l_grid[i], bg = "greenyellow", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 1024:
				label = Label(grid_frame, text = l_grid[i], bg = "lime", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 2048:
				label = Label(grid_frame, text = l_grid[i], bg = "green", fg = "black", padx = 5, pady = 5, font = ("Arial", 18, 'bold'))
			if l_grid[i] == 4096:
				label = Label(grid_frame, text = l_grid[i], bg = "turquoise", fg = "black", padx = 5, pady = 5)
			label.grid(row = row, column = column, padx = 5, pady = 5, sticky = "nsew")
			grid_frame.grid_columnconfigure(column, weight = 0)
			grid_frame.grid_rowconfigure(row, weight = 0)
			i += 1
	grid_frame.pack(fill="x")
#grid printed

#New number
def full_grid():
	i = 0
	c = 0
	while i < 16:
		if l_grid[i] == 0:
			c += 1
		i += 1
	if c == 0:
		return True
	else:
		return False

def new_number():
	if full_grid() == True:
		print("Lost")
	else:
		i = random.randint(0, 15)
		while l_grid[i] > 0:
			i = random.randint(0, 15)
		if random.randint(0, 11) == 11:
			l_grid[i] = 4
		else:
			l_grid[i] = 2
		print_grid(0)

new_number()
new_number()
update_score()

#Bord update
def copy_bord():
	l_score_copy[0] = l_score[0]
	i = 0
	for i in range(16):
		l_copy[i] = l_grid[i]

def update_bord():
	if l_score[0] > l_score[1]:
		l_score[1] = l_score[0]
		update_score()
	l_grid_intify()
	display_score()
	print_grid(0)
	new_number()
#Number_interactions
def l_grid_intify():
	for i in range(16):
		l_grid[i] = int(l_grid[i])
	
def number_collide():
	pass	

#move events
def move_up(event):
	copy_bord()
	count = 0
	moves = 1
	while moves != 0:
		moves = 0
		i = 4
		while 4 <= i <= 15:
			try:
				if l_grid[i - 4] == 0 and l_grid[i] > 0:
					l_grid[i - 4] = l_grid[i]
					l_grid[i] = 0
					moves += 1
				elif l_grid[i - 4] == l_grid[i] and l_grid[i] > 0:
					l_grid[i] = 0
					l_score[0] += l_grid[i - 4]
					l_grid[i - 4] *= 2
					l_grid[i - 4] = str(l_grid[i - 4])
					moves += 1
			except:
				pass
			i += 1
		count += 1
	if count >= 2:
		update_bord()
	else:
		pass

def move_down(event):
	copy_bord()
	count = 0
	moves = 1
	while moves != 0:
		moves = 0
		i = 11
		while 0 <= i <= 11:
			try:
				if l_grid[i + 4] == 0 and l_grid[i] > 0:
					l_grid[i + 4] = l_grid[i]
					l_grid[i] = 0
					moves += 1
				elif l_grid[i + 4] == l_grid[i] and l_grid[i] > 0:
					l_grid[i] = 0
					l_score[0] += l_grid[i + 4]
					l_grid[i + 4] *= 2
					l_grid[i + 4] = str(l_grid[i + 4])
					moves += 1
			except:
				pass
			i -= 1
		count += 1
	if count >= 2:
		update_bord()
	else:
		pass

def move_right(event):
	copy_bord()
	count = 0
	moves = 1
	while moves != 0:
		moves = 0
		i = 14
		while 0 <= i <= 14:
			try:
				if l_grid[i + 1] == 0 and l_grid[i] > 0:
					l_grid[i + 1] = l_grid[i]
					l_grid[i] = 0
					moves += 1
				elif l_grid[i + 1] == l_grid[i] and l_grid[i] > 0:
					l_grid[i] = 0
					l_score[0] += l_grid[i + 1]
					l_grid[i + 1] *= 2
					l_grid[i + 1] = str(l_grid[i + 1])
					moves += 1
			except:
				pass
			i -= 1
			if i == 11 or i == 7 or i == 3:
				i -= 1
		count += 1
	if count >= 2:
		update_bord()
	else:
		pass

def move_left(event):
	copy_bord()
	count = 0
	moves = 1
	while moves != 0:
		moves = 0
		i = 1
		while 0 <= i <= 15:
			try:
				if l_grid[i - 1] == 0 and l_grid[i] > 0:
					l_grid[i - 1] = l_grid[i]
					l_grid[i] = 0
					moves += 1
				elif l_grid[i - 1] == l_grid[i] and l_grid[i] > 0:
					l_grid[i] = 0
					l_score[0] += l_grid[i - 1]
					l_grid[i - 1] *= 2
					l_grid[i - 1] = str(l_grid[i - 1])
					moves += 1
			except:
				pass
			i += 1
			if i == 12 or i == 8 or i == 4:
				i += 1
		count += 1
	if count >= 2:
		update_bord()
	else:
		pass

def restart(event):
	l_score[0] = 0
	i = 0
	for i in range(16):
		l_grid[i] = 0
	new_number()
	update_bord()

def go_back(event):
	l_score[0] = l_score_copy[0]
	i = 0
	for i in range(16):
		l_grid[i] = l_copy[i]
	print_grid(0)
	
#end
	
#Event binds
app.bind_all('<Up>', move_up)
app.bind_all('<Down>', move_down)
app.bind_all('<Right>', move_right)
app.bind_all('<Left>', move_left)
app.bind_all('<r>', restart)
app.bind_all('<BackSpace>', go_back)
# end

#mainloop
app.mainloop()