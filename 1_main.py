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
import socket
import vlc
import pyautogui
from pynput import keyboard
import cv2

############### 0. Setup
#Declare movie & game files as global vars:
LoadedMovie = "Assets\war.mp4"
Game1 = "Assets\game1.txt"
Game2 = "Assets\game2.txt"
instructionsSource = "Assets\instructions.jpg"
GameStatus = False
checkedTheGame = False
TimerCycle = 0
theStartingMinute = -1
#Set up VLC and start
inst = vlc.Instance(['--video-on-top'])   
PlayMovie = inst.media_player_new(LoadedMovie)   
PlayMovie.set_fullscreen(True)
PlayMovie.play()
##################### 0. Main Loop
theStartingMinute = dt.datetime.now().minute
print(theStartingMinute)
def CheckSeconds_loop(a):
	time.sleep(1)
	GameStatus = a
#	theStartingMinute = 0
	print("1//starting_main")
	################ 1. 1-second loop
	global theStartingMinute
	currentHour = dt.datetime.now().hour
	currentMinute = dt.datetime.now().minute
	currentSecond = dt.datetime.now().second
	print("2//Beginning of Program")
	print("Hour:" + str(currentHour))
	print("Minute:" + str(currentMinute))
	print("Second:" + str(currentSecond))					
	###############  2. Check Instructions
	print("2//CurrentSecond" + str(currentSecond))
	print(GameStatus)
	if currentSecond > 21 and currentSecond < 23 and GameStatus == False:
		PlayMovie.stop()
		GameStatus = True
		global theStartingMinute
	       # open GUI to capture user input
		print("3//instructions triggered")
		print(GameStatus)
		instructionsPic = cv2.imread(instructionsSource)
		cv2.namedWindow("WindowName",cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty("WindowName",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
		cv2.imshow("WindowName",instructionsPic)
		TimerCycle = 0
		key=cv2.waitKey(0)
		theStartingMinute = currentMinute
		print("Captured startingminute")
	############################ A. Pick 1979
		if key==49:
	            print(key)
	            cv2.destroyAllWindows()
	            subprocess.Popen([Game1], shell=True)
	############################ B. Pick Fortnite
		elif key==50:
	            print(key)
	            cv2.destroyAllWindows()
	            subprocess.Popen([Game2], shell=True)
		else:
			print(key)
	elif GameStatus == True:
		print("Playing Game Now")
		theStartingMinute
		print(theStartingMinute)
		print("startingMinute")
		if currentMinute > theStartingMinute+1:
			print("Closing Game Now")
			os.system("taskkill /im notepad.exe")
			time.sleep(3)
			GameStatus = False
			theStartingMinute = currentMinute
			PlayMovie.play()
	else:
		print("1//exit" + str(currentSecond))
	print(GameStatus)
	print("////////endmainloop")
	return GameStatus
		################ 1.-exit Time loop
while True:
	PlayState = CheckSeconds_loop(GameStatus)
	print(PlayState)
	print("////////STARTmainloop")

	if PlayState == True:
		print(GameStatus)
		GameStatus = CheckSeconds_loop(PlayState)
		print("loopyplay")
	else:
		PlayState = False
		GameStatus = False
		print("PlayingMovie")
		
	