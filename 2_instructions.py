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
import socket #used for WiFi connection checker 
from pynput import keyboard
import cv2

instructionsSource = "Assets\instructions.jpg"
Game1 = "Assets\game1.txt"
Game2 = "Assets\game2.txt"

def instructions():
    #def Function(Instructions)
            # open GUI to capture user input
        instructionsPic = cv2.imread(instructionsSource)
        cv2.namedWindow("WindowName",cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("WindowName",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("WindowName",instructionsPic)

        key=cv2.waitKey(0)
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
        # if gameChoice == 'f':
        #     print("You chose to play Fortnite.")        
        #     subprocess.Popen([Game1], shell=True)
        #     # sleep for the length of time in seconds you want gameplay to go on ... 
        #     #i've set this to 5 seconds for testing purposes, 900 seconds (15 minutes) might be good for installation 
        #     time.sleep(5)
        # elif gameChoice == 'w':
        #     print("You chose to play 1979")
        #     subprocess.Popen([Game2], shell=True)
        #     time.sleep(5)
instructions()       