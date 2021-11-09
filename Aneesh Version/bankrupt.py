# -*- coding: utf-8 -*-
"""Bankrupt

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19s9g1BH65pG1EgVevLiF9islpAToAAqE
"""

import pygame, sys
from pygame.locals import *

#Important Variables
money = 999999999
netRate = 0
spending_rate = 1
EXP = 0

#Creating Display Window
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Bankrupt")


font = pygame.font.Font('freesansbold.ttf', 30)
smaller_font = pygame.font.Font('freesansbold.ttf', 20)
bigger_font = pygame.font.Font('freesansbold.ttf', 60)

def backgroundColor(screen, money):
    r = money/999999999 * 255
    g = (999999999 - money)/999999999 * 255
    screen.fill((r, g, 0))

class Game_State():
    def __init__(self):
        self.state = 'Main_Game'

    def Menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def Main_Game(self):
        global money
        global spending_rate
        global EXP
        global game_state

        backgroundColor(screen, money)
        #Black Background
        pygame.draw.rect(screen, (0, 140, 170), (390, 300, 120, 60))
        pygame.draw.rect(screen, (246, 246, 246), (900, 0, 380, 720))
        #Spend Button
        pygame.draw.rect(screen, (208, 208, 208), (940, 50, 300, 50))
        #Upgrades
        pygame.draw.rect(screen, (208, 208, 208), (940, 150, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 275, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 400, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 525, 140, 100))
        pygame.draw.rect(screen, (208, 208, 208), (1100, 525, 140, 100))

        text = font.render('Spend', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (400, 310)
        screen.blit(text, text_rect)

        text = font.render('$' + str(money), False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (450 - (text_rect[2] / 2), 260)
        screen.blit(text, text_rect)

        text = font.render('EXP: ' + str(EXP), False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 62)
        screen.blit(text, text_rect)

        text = font.render('Upgrades', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 187)
        screen.blit(text, text_rect)

        text = font.render('Advanced', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 295)
        screen.blit(text, text_rect)

        text = font.render('Upgrades', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 325)
        screen.blit(text, text_rect)

        text = font.render('Boosts', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 432)
        screen.blit(text, text_rect)

        text = smaller_font.render('Pause', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1010 - (text_rect[2] / 2), 562)
        screen.blit(text, text_rect)

        text = smaller_font.render('Home', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1170 - (text_rect[2] / 2), 562)
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 510 and 300 <= mouse[1] <= 350:
                    money -= spending_rate
                    EXP += 1
                elif 940 <= mouse[0] <= 1240 and 150 <= mouse[1] <= 250:
                    self.state = 'Upgrades'
                elif 940 <= mouse[0] <= 1240 and 275 <= mouse[1] <= 375:
                    self.state = 'Lucky Upgrades'

                elif 940 <= mouse[0] <= 1240 and 400 <= mouse[1] <= 500:
                    if EXP >= 10000:
                        EXP -= 10000
                        spending_rate *= 1.05

    def Upgrades(self):
        global money
        global spending_rate
        global EXP
        global game_state
        backgroundColor(screen, money)
        pygame.draw.rect(screen, (0, 140, 170), (390, 200, 120, 60))
        pygame.draw.rect(screen, (246, 246, 246), (900, 0, 380, 720))
        pygame.draw.rect(screen, (208, 208, 208), (940, 50, 300, 50))
        pygame.draw.rect(screen, (208, 208, 208), (940, 150, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 275, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 400, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 525, 140, 100))
        pygame.draw.rect(screen, (208, 208, 208), (1100, 525, 140, 100))
        pygame.draw.rect(screen, (246, 246, 246), (0, 400, 900, 320))
        #upgrade buttons
        pygame.draw.rect(screen, (208, 208, 208), (20, 420, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (20, 570, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (200, 420, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (200, 570, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (380, 420, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (20, 280, 150, 80))


        text = font.render('Spend', False, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topleft = (400, 210)
        screen.blit(text, text_rect)

        text = font.render('$' + str(money), False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (450 - (text_rect[2] / 2), 160)
        screen.blit(text, text_rect)

        text = font.render('EXP: ' + str(EXP), False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 62)
        screen.blit(text, text_rect)

        text = font.render('Upgrades', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 187)
        screen.blit(text, text_rect)

        text = font.render('Advanced', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 295)
        screen.blit(text, text_rect)

        text = font.render('Upgrades', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 325)
        screen.blit(text, text_rect)

        text = font.render('Boosts', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 432)
        screen.blit(text, text_rect)

        text = smaller_font.render('Pause', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1010 - (text_rect[2] / 2), 562)
        screen.blit(text, text_rect)

        text = smaller_font.render('Home', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1170 - (text_rect[2] / 2), 562)
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 510 and 180 <= mouse[1] <= 240:
                    money -= spending_rate
                    EXP += 1
                elif 940 <= mouse[0] <= 1240 and 275 <= mouse[1] <= 375:
                    self.state = 'Lucky Upgrades'
                elif 20 <= mouse[0] <= 170 and 280 <= mouse[1] <= 360:
                    self.state = 'Main_Game'

                elif 940 <= mouse[0] <= 1240 and 400 <= mouse[1] <= 500:
                    if EXP >= 10000:
                        EXP -= 10000
                        spending_rate *= 1.05

    def Lucky_Upgrades(self):
        global money
        global spending_rate
        global EXP
        global game_state
        backgroundColor(screen, money)
        pygame.draw.rect(screen, (0, 140, 170), (390, 200, 120, 60))
        pygame.draw.rect(screen, (246, 246, 246), (900, 0, 380, 720))
        pygame.draw.rect(screen, (208, 208, 208), (940, 50, 300, 50))
        pygame.draw.rect(screen, (208, 208, 208), (940, 150, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 275, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 400, 300, 100))
        pygame.draw.rect(screen, (208, 208, 208), (940, 525, 140, 100))
        pygame.draw.rect(screen, (208, 208, 208), (1100, 525, 140, 100))
        pygame.draw.rect(screen, (246, 246, 246), (0, 400, 900, 320))
        # upgrade buttons
        pygame.draw.rect(screen, (208, 208, 208), (20, 420, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (20, 570, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (200, 420, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (200, 570, 150, 80))
        pygame.draw.rect(screen, (208, 208, 208), (380, 420, 150, 80))
        # lucky upgrade buttons

        text = font.render('Spend', False, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topleft = (400, 210)
        screen.blit(text, text_rect)

        text = font.render('$' + str(money), False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (450 - (text_rect[2] / 2), 160)
        screen.blit(text, text_rect)

        text = font.render('EXP: ' + str(EXP), False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 62)
        screen.blit(text, text_rect)

        text = font.render('Upgrades', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 187)
        screen.blit(text, text_rect)

        text = font.render('Advanced', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 295)
        screen.blit(text, text_rect)

        text = font.render('Upgrades', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 325)
        screen.blit(text, text_rect)

        text = font.render('Boosts', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1090 - (text_rect[2] / 2), 432)
        screen.blit(text, text_rect)

        text = smaller_font.render('Pause', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1010 - (text_rect[2] / 2), 562)
        screen.blit(text, text_rect)

        text = smaller_font.render('Home', False, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (1170 - (text_rect[2] / 2), 562)
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 510 and 180 <= mouse[1] <= 240:
                    money -= spending_rate
                    EXP += 1
                elif 940 <= mouse[0] <= 1240 and 150 <= mouse[1] <= 250:
                    self.state = 'Upgrades'

                elif 20 <= mouse[0] <= 170 and 280 <= mouse[1] <= 360:
                    self.state = 'Main_Game'

                elif 940 <= mouse[0] <= 1240 and 400 <= mouse[1] <= 500:
                    if EXP >= 10000:
                        EXP -= 10000
                        spending_rate *= 1.05

    def State_Manager(self):
        if self.state == 'Menu':
            self.Menu()
        elif self.state == 'Main_Game':
            self.Main_Game()
        elif self.state == "Upgrades":
            self.Upgrades()
        elif self.state == "Lucky Upgrades":
            self.Lucky_Upgrades()


game_state = Game_State()

while True:
    game_state.State_Manager()
    mouse = pygame.mouse.get_pos()
    pygame.display.update()