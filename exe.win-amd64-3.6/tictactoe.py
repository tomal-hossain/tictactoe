import pygame
import sys
import random
import time

pygame.init()

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tictactoe")
fps = pygame.time.Clock()

background = (128,255,255)
box = (255,255,255)
boxPos = [[5,5],[205,5],[405,5],[5,205],[205,205],[405,205],[5,405],[205,405],[405,405]]
userColor = (230,0,14)
computerColor = (0,230,0)
message = (0,162,232)

userMove = pygame.mixer.Sound("userMove.wav")
drawSound = pygame.mixer.Sound("draw.wav")
defeat = pygame.mixer.Sound("Lost.wav")

selected = []
user = []
computer = []
value = [0,0,0,0,0,0,0,0,0,0]
drawSign = [[-600,-600],[50,50],[250,50],[450,50],[50,250],[250,250],[450,250],[50,450],[250,450],[450,450]]
draw = 0
loose = 0


def checkComputer(pos):
	global selected
	for val in selected:
		if val == pos:
			return 0
	return 1

def checkUser(pos):
	global user
	global selected
	flag = 1
	for val in selected:
		if val == pos:
			flag = 0
			break
	if flag == 1:
		pygame.mixer.Sound.play(userMove)
		user.append(pos)
		selected.append(pos)
		ComputerSelect(pos)

def ComputerSelect(pos):
	global selected
	global computer
	global user
	global loose
	global draw
	global value
	flag = 1
	for val in selected:
		if val == 5:
			flag = 0
			break
	if flag == 1:
		computer.append(5)
		selected.append(5)
	else:
		if pos == 5:
			if computer[0] == 1 or computer[0]== 9:
				choice = random.randrange(1,100)
				if choice < 50:
					computer.append(3)
					selected.append(3)
				else:
					computer.append(7)
					selected.append(7)
			else:
				choice = random.randrange(1,100)
				if choice < 50:
					computer.append(1)
					selected.append(1)
				else:
					computer.append(9)
					selected.append(9)
		elif len(selected)==4:
			if user[0]==5:
				if computer[0]==9:
					if computer[1]==3:
						flag=checkComputer(6)
						if flag == 1:
							computer.append(6)
							selected.append(6)
							loose = 1
						else:
							computer.append(4)
							selected.append(4)
					elif computer[1]==7:
						flag=checkComputer(8)
						if flag == 1:
							computer.append(8)
							selected.append(8)
							loose = 1
						else:
							computer.append(2)
							selected.append(2)
				elif computer[0]==1:
					if computer[1]==3:
						flag=checkComputer(2)
						if flag == 1:
							computer.append(2)
							selected.append(2)
							loose = 1
						else:
							computer.append(8)
							selected.append(8)
					elif computer[1]==7:
						flag=checkComputer(4)
						if flag == 1:
							computer.append(4)
							selected.append(4)
							loose = 1
						else:
							computer.append(6)
							selected.append(6)
				elif computer[0]==3:
					if computer[1]==1:
						flag=checkComputer(2)
						if flag == 1:
							computer.append(2)
							selected.append(2)
							loose = 1
						else:
							computer.append(8)
							selected.append(8)
					elif computer[1]==9:
						flag=checkComputer(6)
						if flag == 1:
							computer.append(6)
							selected.append(6)
							loose = 1
						else:
							computer.append(4)
							selected.append(4)
				elif computer[0]==7:
					if computer[1]==1:
						flag=checkComputer(4)
						if flag == 1:
							computer.append(4)
							selected.append(4)
							loose = 1
						else:
							computer.append(6)
							selected.append(6)
					elif computer[1]==9:
						flag=checkComputer(8)
						if flag == 1:
							computer.append(8)
							selected.append(8)
							loose = 1
						else:
							computer.append(2)
							selected.append(2)
			elif computer[1] == 5:
				if computer[0]==9:
					flag=checkComputer(1)
					if flag == 1:
						computer.append(1)
						selected.append(1)
						loose = 1
					else:
						if user[0] == 2 or pos ==2 and checkComputer(3)==1:
							computer.append(3)
							selected.append(3)
						elif user[0] == 3 or pos == 3 and checkComputer(2)==1:
							computer.append(2)
							selected.append(2)
						elif user[0] == 4 or pos ==4 and checkComputer(7)==1:
							computer.append(7)
							selected.append(7)
						elif user[0] == 7 or pos == 7 and checkComputer(4)==1:
							computer.append(4)
							selected.append(4)
						else:
							if user[0]==6 or pos == 6:
								computer.append(7)
								selected.append(7)
							else:
								computer.append(3)
								selected.append(3)

				if computer[0]==1:
					flag=checkComputer(9)
					if flag == 1:
						computer.append(9)
						selected.append(9)
						loose = 1
					else:
						if user[0] == 3 or pos ==3 and checkComputer(6)==1:
							computer.append(6)
							selected.append(6)
						elif user[0] == 6 or pos == 6 and checkComputer(3)==1:
							computer.append(3)
							selected.append(3)
						elif user[0] == 8 or pos ==8 and checkComputer(7)==1:
							computer.append(7)
							selected.append(7)
						elif user[0] == 7 or pos == 7 and checkComputer(8)==1:
							computer.append(8)
							selected.append(8)
						else:
							if user[0]==2 or pos == 2:
								computer.append(7)
								selected.append(7)
							else:
								computer.append(3)
								selected.append(3)
				if computer[0]==3:
					flag=checkComputer(7)
					if flag == 1:
						computer.append(7)
						selected.append(7)
						loose = 1
					else:
						if user[0] == 8 or pos ==8 and checkComputer(9)==1:
							computer.append(9)
							selected.append(9)
						elif user[0] == 1 or pos == 1 and checkComputer(4)==1:
							computer.append(4)
							selected.append(4)
						elif user[0] == 4 or pos ==4 and checkComputer(1)==1:
							computer.append(1)
							selected.append(1)
						elif user[0] == 9 or pos == 9 and checkComputer(8)==1:
							computer.append(8)
							selected.append(8)
						else:
							if user[0]==2 or pos == 2:
								computer.append(9)
								selected.append(9)
							else:
								computer.append(1)
								selected.append(1)
				if computer[0]==7:
					flag=checkComputer(3)
					if flag == 1:
						computer.append(3)
						selected.append(3)
						loose = 1
					else:
						if user[0] == 2 or pos ==2 and checkComputer(1)==1:
							computer.append(1)
							selected.append(1)
						elif user[0] == 1 or pos == 1 and checkComputer(2)==1:
							computer.append(2)
							selected.append(2)
						elif user[0] == 6 or pos ==6 and checkComputer(9)==1:
							computer.append(9)
							selected.append(9)
						elif user[0] == 9 or pos == 9 and checkComputer(6)==1:
							computer.append(6)
							selected.append(6)
						else:
							if user[0]==4 or pos == 4:
								computer.append(9)
								selected.append(9)
							else:
								computer.append(1)
								selected.append(1)
		elif len(selected)==6:
			if computer[1]==5:
				if computer[2] == 8 and checkComputer(2)==1:
					computer.append(2)
					selected.append(2)
					loose = 1
				elif computer[2] == 2 and checkComputer(8)==1:
					computer.append(8)
					selected.append(8)
					loose = 1
				elif computer[2] == 6 and checkComputer(4)==1:
					computer.append(4)
					selected.append(4)
					loose = 1
				elif computer[2] == 4 and checkComputer(6)==1:
					computer.append(6)
					selected.append(6)
					loose = 1
				elif computer[2]==3 and computer[0]==9:
					if checkComputer(6)==1:
						computer.append(6)
						selected.append(6)
						loose = 1
					elif checkComputer(7)==1:
						computer.append(7)
						selected.append(7)
						loose = 1
				elif computer[2]==3 and computer[0]==1:
					if checkComputer(2)==1:
						computer.append(2)
						selected.append(2)
						loose = 1
					elif checkComputer(7)==1:
						computer.append(7)
						selected.append(7)
						loose = 1
				elif computer[2]==1 and computer[0]==7:
					if checkComputer(4)==1:
						computer.append(4)
						selected.append(4)
						loose = 1
					elif checkComputer(9)==1:
						computer.append(9)
						selected.append(9)
						loose = 1
				elif computer[2]==1 and computer[0]==3:
					if checkComputer(2)==1:
						computer.append(2)
						selected.append(2)
						loose = 1
					elif checkComputer(9)==1:
						computer.append(9)
						selected.append(9)
						loose = 1
				elif computer[2]==7 and computer[0]==1:
					if checkComputer(4)==1:
						computer.append(4)
						selected.append(4)
						loose = 1
					elif checkComputer(3)==1:
						computer.append(3)
						selected.append(3)
						loose = 1
				elif computer[2]==7 and computer[0]==9:
					if checkComputer(8)==1:
						computer.append(8)
						selected.append(8)
						loose = 1
					elif checkComputer(3)==1:
						computer.append(3)
						selected.append(3)
						loose = 1
				elif computer[2]==9 and computer[0]==7:
					if checkComputer(1)==1:
						computer.append(1)
						selected.append(1)
						loose = 1
					elif checkComputer(8)==1:
						computer.append(8)
						selected.append(8)
						loose = 1
				elif computer[2]==9 and computer[0]==3:
					if checkComputer(1)==1:
						computer.append(1)
						selected.append(1)
						loose = 1
					elif checkComputer(6)==1:
						computer.append(6)
						selected.append(6)
						loose = 1
				else:
					if checkComputer(2)==1:
						computer.append(2)
						selected.append(2)
					elif checkComputer(6)==1:
						computer.append(6)
						selected.append(6)
					elif checkComputer(8)==1:
						computer.append(8)
						selected.append(8)
					elif checkComputer(4)==1:
						computer.append(4)
						selected.append(4)
			elif user[0]==5:
				if user[2]==2:
					computer.append(8)
					selected.append(8)
				elif user[2]==6:
					computer.append(4)
					selected.append(4)
				elif user[2]==4:
					computer.append(6)
					selected.append(6)
				elif user[2]==8:
					computer.append(2)
					selected.append(2)
				else:
					if checkComputer(1)==1:
						computer.append(1)
						selected.append(1)
					elif checkComputer(3)==1:
						computer.append(3)
						selected.append(3)
					elif checkComputer(7)==1:
						computer.append(7)
						selected.append(7)
					elif checkComputer(9)==1:
						computer.append(9)
						selected.append(9)
		elif len(selected)==8:
			if checkComputer(1)==1:
				computer.append(1)
				selected.append(1)
			elif checkComputer(2)==1:
				computer.append(2)
				selected.append(2)
			elif checkComputer(3)==1:
				computer.append(3)
				selected.append(3)
			elif checkComputer(4)==1:
				computer.append(4)
				selected.append(4)
			elif checkComputer(5)==1:
				computer.append(5)
				selected.append(5)
			elif checkComputer(6)==1:
				computer.append(6)
				selected.append(6)
			elif checkComputer(7)==1:
				computer.append(7)
				selected.append(7)
			elif checkComputer(8)==1:
				computer.append(8)
				selected.append(8)
			elif checkComputer(9)==1:
				computer.append(9)
				selected.append(9)
			for val in computer:
				value[val]=1
			if value[1]==1 and value[2]==1 and value[3]==1:
				loose = 1
			elif value[1]==1 and value[4]==1 and value[7]==1:
				loose = 1
			elif value[7]==1 and value[8]==1 and value[9]==1:
				loose = 1
			elif value[3]==1 and value[6]==1 and value[9]==1:
				loose = 1
			elif value[4]==1 and value[5]==1 and value[6]==1:
				loose = 1
			elif value[2]==1 and value[5]==1 and value[8]==1:
				loose = 1
			else:
				draw = 1



def newSelect (pos):
	if (5<pos[0]<195 and 5<pos[1]<195):
		checkUser(1)
	elif (205<pos[0]<395 and 5<pos[1]<195):
		checkUser(2)
	elif (405<pos[0]<595 and 5<pos[1]<195):
		checkUser(3)
	elif (5<pos[0]<195 and 205<pos[1]<395):
		checkUser(4)
	elif (205<pos[0]<395 and 205<pos[1]<395):
		checkUser(5)
	elif (405<pos[0]<595 and 205<pos[1]<395):
		checkUser(6)
	elif (5<pos[0]<195 and 395<pos[1]<595):
		checkUser(7)
	elif (205<pos[0]<395 and 395<pos[1]<595):
		checkUser(8)
	elif (405<pos[0]<595 and 395<pos[1]<595):
		checkUser(9)
def Button(action=None):
	pos = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if 230<pos[0]<350 and 550<pos[1]<590:
		pygame.draw.rect(surface,computerColor,[230,550,120,40])
		if click[0]==1 and action!=None:
			action()
	else:
		pygame.draw.rect(surface,message,[230,550,120,40])
	font = pygame.font.SysFont("comicsansms",20)
	text = font.render("Play Again",True,background)
	surface.blit(text,(245,555))


def GameOver():
	pygame.mixer.Sound.play(defeat)
	font = pygame.font.SysFont("comicsansms",80)
	text = font.render("You Loose!",True,message)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		surface.blit(text,(100,180))
		Button(PlayAgain)
		pygame.display.update()
		fps.tick(10)

def MatchDraw():
	pygame.mixer.Sound.play(drawSound)
	font = pygame.font.SysFont("comicsansms",80)
	text = font.render("Match Tied",True,message)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		surface.blit(text,(100,180))
		Button(PlayAgain)
		pygame.display.update()
		fps.tick(10)

def PlayAgain():
	global computer
	global selected
	global user
	global draw
	global loose
	global value
	computer = []
	selected = []
	user = []
	draw = 0
	loose = 0
	value = [0,0,0,0,0,0,0,0,0,0]
	time.sleep(1)
	MainLoop()

def drawUser():
	global user
	global drawSign

	font = pygame.font.SysFont("comicsansms",80)
	zero = font.render("0",True,userColor)

	for val in user:
		surface.blit(zero,(drawSign[val]))

def drawComputer():
	global computer
	global drawSign

	font = pygame.font.SysFont("comicsansms",80)
	zero = font.render("X",True,computerColor)

	for val in computer:
		surface.blit(zero,(drawSign[val]))

	
def MainLoop():
	global computer
	global selected
	global boxPos
	global loose
	global draw

	choice = random.randrange(1,100)
	if choice < 25:
			computer.append(1)
			selected.append(1)
	elif choice <50:
			computer.append(3)
			selected.append(3)
	elif choice <75:
			computer.append(7)
			selected.append(7)
	else:
		computer.append(9)
		selected.append(9)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		surface.fill(background)
		for pos in boxPos:
			pygame.draw.rect(surface,box,[pos[0],pos[1],190,190])
		drawComputer()
		drawUser()
		if loose==1:
			GameOver()
		if draw==1:
			MatchDraw()
		pos = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		if click[0] == 1:
			newSelect(pos)

		pygame.display.update()
		fps.tick(10)
MainLoop()
pygame.quit()
sys.exit()