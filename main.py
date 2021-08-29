import sys
import random
import curses
import numpy as np
from time import sleep
from os import system, name


import keyboard



def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


tetMap = np.zeros((40,10),'U3')
tetMap.fill(' . ')

clearLine = np.zeros((1,10),'U3')
clearLine.fill(' . ')

S_Shape = np.zeros((4,2),'U1')
S_Shape = np.array([[' []',' . ',' . ',' . '],[' []',' []',' []',' . ']])

Z_Shape = np.zeros((4,2),'U1')
Z_Shape = np.array([[' []',' []',' . ',' . '],[' . ',' []',' []',' . ']])

T_Shape = np.zeros((4,2),'U1')
T_Shape = np.array([[' . ',' []',' . ',' . '],[' []',' []',' []',' . ']])

L_Shape = np.zeros((4,2),'U1')
L_Shape = np.array([[' . ',' . ',' []',' . '],[' []',' []',' []',' . ']])

Mirrored_L_Shape = np.zeros((4,2),'U1')
Mirrored_L_Shape = np.array([[' []',' . ',' . ',' . '],[' []',' []',' []',' . ']])

Line_Shape = np.zeros((4,2),'U1')
Line_Shape = np.array([[' . ',' . ',' . ',' . '],[' []',' []',' []',' []']])

Square_Shape = np.zeros((4,2),'U1')
Square_Shape = np.array([[' []',' []',' . ',' . '],[' []',' []',' . ',' . ']])





"""
def intit_peace(peace,x1):

	print(str(tetMap).replace("'"," "))
	sleep(0.5)
	clear()

	tetMap[x1,4] = peace[1,0]
	tetMap[x1,5] = peace[1,1]
	tetMap[x1,6] = peace[1,2]
	tetMap[x1,7] = peace[1,3]
	
	print(str(tetMap).replace("'"," "))
	sleep(0.5)
	clear()
	
	x0 = x1
	x1 += 1

	tetMap[x1,4] = peace[1,0]
	tetMap[x1,5] = peace[1,1]
	tetMap[x1,6] = peace[1,2]
	tetMap[x1,7] = peace[1,3]

	tetMap[x0,4] = peace[0,0]
	tetMap[x0,5] = peace[0,1]
	tetMap[x0,6] = peace[0,2]
	tetMap[x0,7] = peace[0,3]

	print(str(tetMap).replace("'"," "))

	return x1
"""


def random_peaces():

	peacesList = [S_Shape, Z_Shape, T_Shape, L_Shape, Mirrored_L_Shape, Line_Shape, Square_Shape]

	return peacesList[random.randint(0,6)]





def move_down(peace,x1,x0,pos):
	
	clear()
	
	tetMap[x1,pos] = peace[1,0]
	tetMap[x1,pos+1] = peace[1,1]
	tetMap[x1,pos+2] = peace[1,2]
	tetMap[x1,pos+3] = peace[1,3]
	if x1 > 0 :
		tetMap[x0,pos] = peace[0,0]
		tetMap[x0,pos+1] = peace[0,1]
		tetMap[x0,pos+2] = peace[0,2]
		tetMap[x0,pos+3] = peace[0,3]
	if x0-1 >= 0 :
		tetMap[x0-1] = clearLine
		#tetMap[x0-1,pos] = ' . '
		#tetMap[x0-1,pos+1] = ' . '
		#tetMap[x0-1,pos+2] = ' . '
		#tetMap[x0-1,pos+3] = ' . '

	print(str(tetMap).replace("'"," "))
	print(x1,x0)





limit = 40
array =  np.zeros((40,10),'U3')
x1 = 0
x0 = 0
pos = 3



while True:
	

	clear()

	peace = random_peaces()
	
	#peace = Line_Shape

	#comp = peace == Line_Shape

	pos = 3
	x1 = 0
	x0 = 0
#	x1 = intit_peace(peace,x1)


	while True:

		sleep(0)
		if x1 == 40:
			break

		elif ( tetMap[x1,pos] == ' . ' and tetMap[x1,pos+1] == ' . ' and tetMap[x1,pos+2] == ' . ' and tetMap[x1,pos+3] == ' . ') and ( x1 < limit ):
			#if comp.all()  and tetMap[x1,pos+3] == ' . ':
			move_down(peace,x1,x0,pos)

		else :
			break

		x0 = x1
		x1 += 1

		if keyboard.is_pressed('left') and pos >= 0:
			pos -= 1
		elif keyboard.is_pressed('right') and pos <= 9:
			pos += 1
		

	#tetMap = move_down(peace,x1,x0,pos)
	clear()
	print(str(tetMap).replace("'"," "))
	#break

#print(str(tetMap).replace("'"," "))
print(x1,x0)


				
		#if keyboard.is_pressed(''):