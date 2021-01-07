import pygame
import os
import random
import sys


class Settings:                                                         #Hier werden die Einstellungen eingesetzt (Fenstergrößen, Geschwindigkeit, Ort der Fotos usw)
    def _init_(self):
        self.width = 1000
        self.height = 600
        self.border = 10
        self.fps = 60
        self.punkte = 0
        self.TIME_EVENT = pygame.USEREVENT + 1
        self.SPEED_UP = 0;
        self.file_path = os.path.dirname(os.path.abspath(_file_))
        self.images_path = os.path.join(self.file_path, "images")           #ermittelt wo der file ist

    def get_dim(self):
        return (self.width, self.height)


class Figur(pygame.sprite.Sprite):                                                  #Hier wird die Figur konfiguriert und als Bitmap konvertiert
    def _init_(self, pygame, settings):
        super(Figur, self)._init_()
        self.settings = settings
        self.pygame = pygame
        self.image = self.pygame.image.load(os.path.join(self.settings.images_path, "Affe.png")).convert_alpha() #Figur wird scaliert und transformtiert
        self.image = self.pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.fenster_width  // 2
        self.rect.centerx = Setting.fenster_height // 2
        self.rect.bottom = Settings.fenster_height - Settings.fenster_border
        self.direction = 0
        self.speed = 3
        

    def position(self, x, y):                                           #Hier werden die X und Y achsen eingestellt
        figur.rect.x = x
        figur.rect.y = y
        return not pygame.sprite.spritecollideany(figur, all_bananes)


    def update(self):                                                       #Das ist das Programm, welches die Figuren nicht aus dem Fenster rauslässt
        neurect = self.rect.move (self.direction * self.speed, 0)
        if neurect.left <= Settings.fenster_border:
            self.move_stop()
        if neurect.right >= Settings.fenster_width - Settings.fenster_border:
            self.move_stop()
        self.rect.move_ip(self.direction * self.speed, 0)

    def update(self):                                                   #Hier wird definiert wo und in welcher richtung die figur gehen kann. x_y.
        keys = pygame.key.get_pressed()
        if keys[pygame].K_LEFT:    
            self.rect.x -= 3
        if keys[pygame].K_RIGHT:   
            self.rect.x += 3
        if keys[pygame].K_DOWN:    
            self.rect.y += 3
        if keys[pygame].K_UP:      
            self.rect.y -= 3

    def springen(self):                                                              
        while (True):                                                                           
            x = random.randrange(0, self.settings.width - self.rect.width)              
            y = random.randrange(0, self.settings.height - self.rect.height)
            if (self.istPositionFrei(x, y)):
                self.rect.x = x
                self.rect.y = y
                break


class Punktstand(pygame.sprite.Sprite):                                                     #Hier wird programmiert, wie das Bildschirm mit Bestimmten Hintergrundfarrben aussehen soll.
    def _init_(self, pygame, settings):                                                     #Und der Punktstand wird angezeigt
        super(Punktstand, self).__init__()
        self.settings = settings
        self.pygame = pygame
        self.font = pygame.font.SysFont(None, 35)
        self.image = self.font.render(f'punkte: {self.settings.punkte}', True, (250,250 ,250 ))
        self.image = self.pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def update(self):
        self.image = self.font.render(f'punkte: {self.settings.punkte}', True, (250, 250, 250))


class Bananen(pygame.sprite.Sprite):                                                                #Hier werden die Hindernisse wie in der Aufgabenstellung programmiert.
    def _init_(self, pygame, settings):
        super(Bananen, self)._init_()
        self.settings = settings
        self.pygame = pygame
        self.image = self.pygame.image.load(os.path.join(self.settings.images_path, "bananen.png")).convert_alpha()
        size = random.randrange(15, 50)
        self.image = self.pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, settings.width - self.rect.width)
        self.rect.y = random.randrange(-10, 20)
        self.geschwindigkeit = random.randrange(1, 2)

    def Gelbe_banane(self):
        while (True):
            banane = Bananen(pygame, settings)
            if (not pygame.sprite.spritecollideany(banane, all_bananes)):
                all_bananes.add(banane)
                all_sprites.add(all_bananes)
                break
            banane.kill()

    def update(self):
        self.rect.y += self.geschwindigkeit + self.settings.SPEED_UP
        if (self.rect.y + self.rect.height >= self.settings.height):
            self.settings.punkte += 1
            print(f'{self.settings.punkte}')
            self.kill()
            self.Gelbe_banane()


class Game(object):                                             
    def _init_(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.get_dim()
        self.clock = pygame.time.Clock()
        self.figur = Figur(pygame, settings)
        pygame.time.set_timer(self.settings.TIME_EVENT, 2500)
        all_spieler.add(self.figur)
        all_bananes.add(Bananen(pygame, settings))
        all_sprites.add(Punktstand(pygame, settings))
        all_sprites.add(all_bananes, all_spieler)
        self.done = False



if __name__ == '_main_':

    pygame.init()
    screen = pygame.display.set_mode((Settings.fenster_width, Settings.fenster_height))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    all_bananes = pygame.sprite.Group()
    all_spieler = pygame.sprite.Group()
    pygame.display.set_caption("Game1.3")
    figur = Figur("Affe.png")
    all_sprites.add(figur)
    running = True
    while not self.done:
            self.clock.tick(self.settings.fps)
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:                        #Das spiel mit Escape beenden
                        self.done = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:                         #SPACE-Taste loslassen, dann springt das Bitmap an eine neue Zufällig Position
                        self.figur.springen()            
                if event.type == self.settings.TIME_EVENT:
                    for banane in range(random.randrange(1, 3)):
                        all_bananes.add(Bananen(pygame, settings))
                        all_sprites.add(all_bananes)
                        self.settings.SPEED_UP += 1

            self.screen.fill((100, 150, 200))
            if (pygame.sprite.spritecollideany(self.figur, all_bananes)):
                self.done = True

            all_sprites.update()
            all_sprites.draw(self.screen)
            self.pygame.display.flip()
    settings = Settings()
    game = Game(pygame, settings)
    game.run()

    pygame.quit()
