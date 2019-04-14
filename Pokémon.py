import sys, pygame
import time
pygame.init()

size = width, height = 1200, 800
black = (0, 0, 0)
white = (255, 255, 255)
sprites = []


screen = pygame.display.set_mode(size)
screen.fill(black)
pygame.display.set_caption('Pokémon Remodeled')
fontObj = pygame.font.Font('freesansbold.ttf', 32)


textSurfaceObj = fontObj.render('Quit', True, white)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (width/32, height/32)


pikachu = pygame.image.load("Resized_Images/pikachu.jpg")
pikachu_rect = pikachu.get_rect()
sprites.append((pikachu, pikachu_rect))

charizard = pygame.image.load("Resized_Images/charizard.jpg")
charizard_rect = charizard.get_rect()
sprites.append((charizard, charizard_rect))

squirtle = pygame.image.load("Resized_Images/squirtle.jpg")
squirtle_rect = squirtle.get_rect()
sprites.append((squirtle, squirtle_rect))

jigglypuff = pygame.image.load("Resized_Images/jigglypuff.jpg")
jigglypuff_rect = jigglypuff.get_rect()
sprites.append((jigglypuff, jigglypuff_rect))

gengar = pygame.image.load("Resized_Images/gengar.jpg")
gengar_rect = gengar.get_rect()
sprites.append((gengar, gengar_rect))

magnemite = pygame.image.load("Resized_Images/magnemite.jpg")
magnemite_rect = magnemite.get_rect()
sprites.append((magnemite, magnemite_rect))

bulbasaur = pygame.image.load("Resized_Images/bulbasaur.jpg")
bulbasaur_rect = bulbasaur.get_rect()
sprites.append((bulbasaur, bulbasaur_rect))

charmander = pygame.image.load("Resized_Images/charmander.jpg")
charmander_rect = charmander.get_rect()
sprites.append((charmander, charmander_rect))

beedrill = pygame.image.load("Resized_Images/beedrill.jpg")
beedrill_rect = beedrill.get_rect()
sprites.append((beedrill, beedrill_rect))

golem = pygame.image.load("Resized_Images/golem.jpg")
golem_rect = golem.get_rect()
sprites.append((golem, golem_rect))

dewgong = pygame.image.load("Resized_Images/dewgong.jpg")
dewgong_rect = dewgong.get_rect()
sprites.append((dewgong, dewgong_rect))

hypno = pygame.image.load("Resized_Images/hypno.jpg")
hypno_rect = hypno.get_rect()
sprites.append((hypno, hypno_rect))

cleffa = pygame.image.load("Resized_Images/cleffa.jpg")
cleffa_rect = cleffa.get_rect()
sprites.append((cleffa, cleffa_rect))

cutiefly = pygame.image.load("Resized_Images/cutiefly.jpg")
cutiefly_rect = cutiefly.get_rect()
sprites.append((cutiefly, cutiefly_rect))



textSurfaceObj1 = fontObj.render('Welcome to Pokémon Remodeled!', True, white)
textRectObj1 = textSurfaceObj1.get_rect()
textRectObj1.center = (width/2, 5*height/16)

textSurfaceObj2 = fontObj.render('Press Start when you', True, white)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (width/2, 9*height/16)

textSurfaceObj3 = fontObj.render('are ready to begin!', True, white)
textRectObj3 = textSurfaceObj3.get_rect()
textRectObj3.center = (width/2, 5*height/8)

textSurfaceObj4 = fontObj.render('Start', True, white)
textRectObj4 = textSurfaceObj4.get_rect()
textRectObj4.center = (width/2, 3*height/4)



screen.blit(textSurfaceObj1, textRectObj1)
screen.blit(textSurfaceObj2, textRectObj2)
screen.blit(textSurfaceObj3, textRectObj3)
screen.blit(textSurfaceObj4, textRectObj4)
rect_textSurfaceObj4 = pygame.draw.rect(screen, white, pygame.Rect(textRectObj4), 1)
screen.blit(textSurfaceObj, textRectObj)
rect_textSurfaceObj = pygame.draw.rect(screen, white, pygame.Rect(textRectObj), 1)


on = True
while on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			on = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if textRectObj4.collidepoint(pos):
				screen.fill(black)
				sprites[2][1].center = (width/4, height/2)
				screen.blit(sprites[2][0], sprites[2][1])
				sprites[6][1].center = (width/2, height/2)
				screen.blit(sprites[6][0], sprites[6][1])
				sprites[7][1].center = (3*width/4, height/2)
				screen.blit(sprites[7][0], sprites[7][1])
				screen.blit(textSurfaceObj, textRectObj)
				rect_textSurfaceObj = pygame.draw.rect(screen, white, pygame.Rect(textRectObj), 1)
			elif textRectObj.collidepoint(pos):
				on = False
	pygame.display.update()
pygame.quit()
