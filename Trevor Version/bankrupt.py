import os
import pygame, sys
import pickle
from pygame.locals import *

#Important Variables
money = 999999999
netRate = 0
spendingRate = 50000000
EXP = 0

#Save and load
class saveObj:
    def __init__(self):
        self.money = money
        self.netRate = netRate
        self.spendingRate = spendingRate
        self.EXP = EXP

def save():
    currentSave = saveObj()
    with open('save.pickle', 'wb') as saveFile:
        pickle.dump(currentSave, saveFile)

def load():
    if not os.path.exists('save.pickle'):
        save()
    elif os.path.getsize('save.pickle') > 0:
        with open('save.pickle','rb') as saveFile:
            currentSave = pickle.load(saveFile)
            global money; money = currentSave.money
            global netRate; netRate = currentSave.netRate
            global spendingRate; spendingRate = currentSave.spendingRate
            global EXP; EXP = currentSave.EXP
    else:
        save()

#Loading Variables
load()

#Creating Display Window
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Bankrupt")


font = pygame.font.Font('freesansbold.ttf', 30)
smaller_font = pygame.font.Font('freesansbold.ttf', 20)
bigger_font = pygame.font.Font('freesansbold.ttf', 60)

#making background
def backgroundColor(screen, money): 
    r = money/999999999 * 255
    g = (999999999 - money)/999999999 * 255
    screen.fill((r, g, 0))

def interactiveButtons(screen):
    pygame.draw.rect(screen, (0 , 140, 170), (390, 400, 120, 60))
    pygame.draw.rect(screen, (0, 0, 123), (900, 0, 380, 720))
    pygame.draw.rect(screen, (0, 0, 0), (940, 50, 300, 50))
    pygame.draw.rect(screen, (0, 0, 0), (940, 150, 300, 100))
    pygame.draw.rect(screen, (0, 0, 0), (940, 275, 300, 100))
    pygame.draw.rect(screen, (0, 0, 0), (940, 400, 300, 100))
    pygame.draw.rect(screen, (0, 0, 0), (940, 525, 140, 100))
    pygame.draw.rect(screen, (0, 0, 0), (1100, 525, 140, 100))

    text = font.render('Spend', False, (0,0,0))
    text_rect = text.get_rect()
    text_rect.topleft = (400,410)
    screen.blit(text, text_rect)

    text = font.render('$' + str(money), False, (0,0,0))
    text_rect = text.get_rect()
    text_rect.topleft = (450 - (text_rect[2]/2),360)
    screen.blit(text, text_rect)

    text = font.render('EXP: ' + str(EXP), False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1090 - (text_rect[2]/2),62)
    screen.blit(text, text_rect)

    text = font.render('Upgrades', False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1090 - (text_rect[2]/2),187)
    screen.blit(text, text_rect)

    text = font.render('Advanced', False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1090 - (text_rect[2]/2),295)
    screen.blit(text, text_rect)

    text = font.render('Upgrades', False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1090 - (text_rect[2]/2),325)
    screen.blit(text, text_rect)

    text = font.render('Boosts', False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1090 - (text_rect[2]/2),432)
    screen.blit(text, text_rect)

    text = smaller_font.render('Pause', False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1010 - (text_rect[2]/2),562)
    screen.blit(text, text_rect)

    text = smaller_font.render('Home', False, (0,200,0))
    text_rect = text.get_rect()
    text_rect.topleft = (1170 - (text_rect[2]/2),562)
    screen.blit(text, text_rect)

    if money <= 0:
        text = bigger_font.render('GAME OVER', False, (0,0,0))
        text_rect = text.get_rect()
        text_rect.topleft = (450 - (text_rect[2]/2),150)
        screen.blit(text, text_rect)
          
        text = bigger_font.render('YOU WIN!', False, (0,0,0))
        text_rect = text.get_rect()
        text_rect.topleft = (450 - (text_rect[2]/2),200)
        screen.blit(text, text_rect)

while True:
    finished = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save()
            pygame.quit()
            sys.exit()
        
        if money <= 0:
            text = font.render('GAME OVER', False, (0,200,0))
            text_rect = text.get_rect()
            text_rect.topleft = (450 - (text_rect[2]/2),150)
            screen.blit(text, text_rect)
            
            text = font.render('YOU WIN!', False, (0,200,0))
            text_rect = text.get_rect()
            text_rect.topleft = (450 - (text_rect[2]/2),200)
            screen.blit(text, text_rect)
            finished = True
    
        if event.type == pygame.MOUSEBUTTONDOWN and not finished:
            if 390 <= mouse[0]<= 510 and 400 <= mouse[1] <= 520:
                if money <= spendingRate:
                    money = 0
                else:
                    money -= spendingRate
                EXP += 10000
            if 940 <= mouse[0]<= 1240 and 400 <= mouse[1] <= 500:
                if EXP >= 10000:
                    EXP -= 10000
                    spendingRate *= 1.05


    backgroundColor(screen, money)
    interactiveButtons(screen)
    mouse = pygame.mouse.get_pos()

    pygame.display.update()