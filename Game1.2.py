import pygame
import os
import sys
import random

class Settings:
    fenster_width = 1000                                   #fenster breite
    fenster_height = 600                                   #fenster höhe 
    fenster_border = 10
    file_path = os.path.dirname(os.path.abspath(__file__)) #ermittelt selber wo der file ist
    image_path = os.path.join(file_path, "images")
    
class Hintergrund(object):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(Settings.image_path, "Terminator.bmp")) #lädt das Foto
        self.image = pygame.transform.scale(self.image, (Settings.fenster_width, Settings.fenster_height)).convert()#Das Bild wird scaliert und konvertiert
        self.rect = self.image.get_rect()

class Figur(pygame.sprite.Sprite):                      #class Figur. hier wird die figur definiert. 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, "Affe.bmp")) #hier lädt das Bitmap Affe.
        self.image = pygame.transform.scale(self.image, (30,30)).convert_alpha() #hier wird es extra für pygame kovertiert und positioniert.
        self.rect = self.image.get_rect()                                                           
        self.rect.centerx = Settings.fenster_width  // 2
        self.rect.bottom = Settings.fenster_height - Settings.fenster_border
        self.direction = 0
        self.speed = 3

    def update(self):                                                       #Das ist das Programm, welches die Figuren nicht aus dem Fenster rauslässt
        neurect = self.rect.move (self.direction * self.speed, 0)
        if neurect.left <= Settings.fenster_border:
            self.move_stop()
        if neurect.right >= Settings.fenster_width - Settings.fenster_border:
            self.move_stop()
        self.rect.move_ip(self.direction * self.speed, 0)
            
    def move_left(self):        #hier wird definiert wo und in welcher richtung die figur gehen kann. x_y.
        self.direction = -1
    def move_up(self):
        self.direction = -1
    def move_down(self):
        self.direction = 1
    def move_right(self):
        self.direction = 1
    def move_stop(self):
        self.direction = 0
        
if __name__ == '__main__':
    
    pygame.init()

    screen = pygame.display.set_mode((Settings.fenster_width, Settings.fenster_height))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    pygame.display.set_caption("Game1.2")
    #hintergrund = Hintergrund("Terminator.bmp")
    #figur = Figur("Affe.bmp")
    #all_sprites.add(figur)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():            #Hier fängt das spiel an. also hier kann man die figur kontrollieren mit pfeiltasten nach oben, unten, rechts, links.
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    figur.move_up()
                if event.key == pygame.K_DOWN:
                    figur.move_down()
                if event.key == pygame.K_ESCAPE:                    #Das spiel mit Escape beenden
                    running = False
                elif event.key == pygame.K_LEFT:
                    figur.move_left()
                elif event.key == pygame.K_RIGHT:
                    figur.move_right()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #nichts drücken bedeutet die figur nicht bewegen.
                    figur.move_stop()
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    figur.move_stop()
                    
        figur.update()
        
        hintergrund.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
