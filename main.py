#Joshua Hadlock
#A1 programming 2
#Whack a mole game
#I did not cheat


# ---------------------Disclaimer, pseudo code is subject to change as more things are added and removed----------------------------
#This is a game of whack a mole. A series of images will randomly pop up for random amount of times in which the player needs to smack
#the knight before he gets away. There will be settings to allow for different difficulties. Things to keep in mind, sometimes there won't be
#anything on the screen, pictures will pop up randomly at random times, and pictures will disappear randomly at random times if not clicked.
#if you click a space without a guy, you lose the game.

#It should start out with a start screen with the settings option. When clicking start, you'll go to the game described above. When clicking settings
# a menu should pop up in which you can change the difficulty. There will also be a point system
import tkinter as tk
import random

#open up the file to see what the last difficulty played was
game = open("game.txt","r")
past_difficulty = game.readlines()
#difficulty variables + start up variables
difficulty = past_difficulty[0]

#close the file before it destroys something
game.close()

#create a system to change the settings based on the last difficulty
def change_coords():
	global difficulty
	global x_coord
	global y_coord
	global time_intervals
	if difficulty == "Medium":
		x_coord = 5
		y_coord = 5
		time_intervals = 5000
	elif difficulty == "Easy":
		x_coord = 3
		y_coord = 3
		time_intervals = 2000
	elif difficulty =="Hard":
		x_coord = 10
		y_coord = 10
		time_intervals = 1000
	else:
		print("something went wrong")
		
change_coords()


points = 0
end_screen_number = 0

#tkinter window startup
window = tk.Tk()
window.title("Start")
window.geometry("500x600")


#start screen


#create the gameboard to play on click
def start_click():
	global window
	window.destroy()

	window = tk.Tk()
	window.title("Whack a Knight")
	window.geometry("1000x1000")
	#runs the game
	play_game()

#settings screen
def settings_click():
	#variables
	global points
	points = 0
	global end_screen_number
	end_screen_number = 0
	#destroy and create a new window
	global window
	window.destroy()

	window = tk.Tk()
	window.title("settings")
	window.geometry("1000x1000")

	#get all the iamges for the settings screen
	create_settings_images()
	start_images()
	#create the buttons for easy, medium, and hard difficulty
	#easy
	global settings
	settings = settings.zoom(5)
	cool_image = tk.Label(window,image=settings)
	cool_image.grid(columnspan=3,row=0,column=0)
	easy_button = tk.Button(window,command=easy_mode,image=easy_image)
	easy_button.grid(row=1,column=0)

	#medium
	medium_button = tk.Button(window,command=medium_mode,image=medium_image)
	medium_button.grid(row=1,column=1)

	#hard
	hard_button = tk.Button(window,command=hard_mode,image=hard_image)
	hard_button.grid(row=1,column=2)



#images for the title and end screens of the program
#title screen images
def start_images():
	global Title_image
	Title_image = tk.PhotoImage(file='Start_image.png')
	Title_image = Title_image.zoom(5)
	global End_image
	End_image = tk.PhotoImage(file='GG.png')
	End_image = End_image.zoom(5)
	global start
	start = tk.PhotoImage(file='start.png.png')
	start = start.subsample(25)
	global settings
	settings = tk.PhotoImage(file='settings.png.png')
	settings = settings.subsample(25)
start_images()

#create the start image on the title screen
Title = tk.Label(window,image=Title_image)
Title.grid(columnspan=2,row=1,column=5)


#buttons on the first window to start or to change difficulty

#start button
start_button = tk.Button(window,command=start_click,image=start)
start_button.grid(row=5,column=5)

#settings button
settings_button = tk.Button(window,command=settings_click,image=settings)
settings_button.grid(row=5,column=6)

#import images for the settings
def create_settings_images():
	global easy_image
	global medium_image
	global hard_image
	easy_image = tk.PhotoImage(file='Easy.png.png')
	easy_image = easy_image.subsample(50)
	medium_image = tk.PhotoImage(file='Medium.png.png')
	medium_image = medium_image.subsample(50)
	hard_image = tk.PhotoImage(file='Hard.png.png')
	hard_image = hard_image.subsample(50)

#import images for the knights
	
#create images for knight to bonk
def create_images():
	global img
	global img2
	global Img3
	img = tk.PhotoImage(file='AHH.png')
	img = img.subsample(50)
	img2 = tk.PhotoImage(file='bonk-1.png')
	img2 = img2.subsample(50)
	Img3 = tk.PhotoImage(file='Calm-1.png')
	Img3 = Img3.subsample(50)

		#Shows the image to bonk and what happens when it isn't bonked

#show image of enemy
def show_enemy(lbl):

	lbl['image'] = img
	global timer_id
	timer_id = lbl.after(random.randint(0,time_intervals),show_nothing,lbl)
	lbl.timer_id = timer_id


#what happens after you bonk the image (on click of image)
def show_nothing(lbl):
	lbl['image'] = Img3
	global timer_id
	timer_id = lbl.after(random.randint(0,time_intervals),show_enemy,lbl)
	lbl.timer_id = timer_id




#shows what happens after a bonk
def dead_knight(lbl):
	lbl['image'] = img2
	print("successfully clicked")
	global timer_id
	lbl.after_cancel(lbl.timer_id)

	#ends game after you hit every single guy
	global end_screen_number
	end_screen_number += 1
	if end_screen_number == (x_coord * y_coord):
		end_game()
	#lbl.after(random.randint(10000,30000),show_nothing,lbl)


	#figure out what image was clicked
def smacked(event):
	global points
	widget = event.widget
	if widget['image'] == img.name:
		points = int(points) + 1
		dead_knight(widget)
	if widget['image'] == Img3.name:
		end_game()



#Define the difficulty 
		#easy
def easy_mode():
	game = open("game.txt","w")
	game.write("Easy")
	game.close()
	global difficulty
	global x_coord
	global y_coord
	global time_intervals
	difficulty = "Easy"
	x_coord = 3
	y_coord = 3
	time_intervals = 5000
	
	start_click()

#medium
def medium_mode():
	game = open("game.txt","w")
	game.write("Medium")
	game.close()
	global difficulty
	global x_coord
	global y_coord
	global time_intervals
	difficulty = "medium"
	x_coord = 5
	y_coord = 5
	time_intervals = 2000
	start_click()


#hard
def hard_mode():
	game = open("game.txt","w")
	game.write("Hard")
	game.close()
	global difficulty
	global x_coord
	global y_coord
	global time_intervals
	difficulty = "hard"
	x_coord = 10
	y_coord = 10
	time_intervals = 1000
	start_click()


#Game screen
def play_game():
	global Dark_knight
	create_images()
	#create the grid for all the knights
	for x in range(0,x_coord):
		for y in range(0,y_coord):
			Dark_knight = tk.Label(image=img)
			Dark_knight.grid(row=x,column=y)
			#allow the button to be clicked
			Dark_knight.bind("<ButtonPress-1>",smacked)
			show_nothing(Dark_knight)

#End screen
def end_game():
	#call images
	global window
	global points
	#destroy window
	window.destroy()

	#create window
	window = tk.Tk()
	window.title("End title")
	window.geometry("1000x1000")
	start_images()
	#calculate points recieved
	points = str(points)
	#create end image on screen
	global GG
	GG = tk.Label(window,image=End_image)
	GG.grid(columnspan=2,row=0,column=0)
	#show your score
	end_title = tk.Label(window,text="score: " + points)
	end_title.grid(row=1,column=0)
	#give the option to replay the game
	restart = tk.Button(window,command=settings_click,text="restart")
	restart.grid(row=1,column=1)
	
window.mainloop()
	

