# written by Austin Arrington for Carrie Mae Weems - HEAVE Installation 
# needed for opening matplotlib in OSX
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
import subprocess, sys, os, time
from scipy.misc import imread
from pylab import imshow, show 
import tkinter as tk
from tkinter.simpledialog import askstring
import datetime as dt
import pygame
#from moviepy.editor import *
#####################

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
	currentHour = dt.datetime.now().hour
	print("Beginning of Program")
	print("Hour:" + str(currentHour))
	#check if time is between area of interest
	# 12am - 12pm movie time   
	if currentHour >= 0 and currentHour < 12:
		# update settings on video to play movie upon open
		subprocess.Popen(["open", "-g", "war.mov"])
		#sleep for entirety of video and then start over 
		time.sleep(15)
		restart_program()
	#12pm - 1pm game time 1 		
	elif currentHour >= 12 and currentHour < 13:
		# open GUI to capture user input
		imshow(imread('instructions.jpg'))
		show() 
		root = tk.Tk()
		# show askstring dialog without the Tkinter window
		root.withdraw()
		gameChoice = askstring("Choice", "Enter f to play Fortnite or w to play 1979. Enter any other key to watch video. ")
		print(gameChoice) 
		if gameChoice == 'f':
			print("You chose to play Fortnite.")		
			p = subprocess.call(
				["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app"]
			)
			# sleep for 15 mins or 900 secs to enable gameplay 
			time.sleep(900)
			# close subprocess
			p.kill()
			restart_program()
		elif gameChoice == 'w':
			print("You chose to play 1979")
			p = subprocess.call(
				["/usr/bin/open", "-W", "-n", "-a", "/Applications/Calculator.app"]
			)
			time.sleep(900)		
			p.kill()
			restart_program()
		else:
			subprocess.Popen(["open", "-g", "war.mov"])
			time.sleep(15)
			restart_program()
	elif currentHour >= 13 and currentHour < 15:
		subprocess.Popen(["open", "-g", "war.mov"])
		#sleep for entirety of video and then start over 
		time.sleep(15)
		restart_program()
	elif currentHour >= 15 and currentHour < 16:
		imshow(imread('instructions.jpg'))
		show() 
		root = tk.Tk()
		# show askstring dialog without the Tkinter window
		root.withdraw()
		gameChoice = askstring("Choice", "Enter f to play Fortnite or w to play 1979. Enter any other key to watch video. ")
		print(gameChoice) 
		if gameChoice == 'f':
			print("You chose to play Fortnite.")		
			p = subprocess.call(
				["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app"]
			)
			# sleep for 15 mins or 900 secs to enable gameplay 
			time.sleep(900)
			# close subprocess
			p.kill()
			restart_program()
	elif currentHour >= 16 and currentHour > 18:
		subprocess.Popen(["open", "-g", "war.mov"])
		#sleep for entirety of video and then start over 
		time.sleep(15)
		restart_program()
	elif currentHour >= 18 and currentHour < 19:
		imshow(imread('instructions.jpg'))
		show() 
		root = tk.Tk()
		# show askstring dialog without the Tkinter window
		root.withdraw()
		gameChoice = askstring("Choice", "Enter f to play Fortnite or w to play 1979. Enter any other key to watch video. ")
		print(gameChoice) 
		if gameChoice == 'f':
			print("You chose to play Fortnite.")		
			p = subprocess.call(
				["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app"]
			)
			# sleep for 15 mins or 900 secs to enable gameplay 
			time.sleep(900)
			# close subprocess
			p.kill()
			restart_program()							
	else:
		subprocess.Popen(["open", "-g", "war.mov"])
		time.sleep(15)
		restart_program()	
							
					
			
	
