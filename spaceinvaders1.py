import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255,0,0)

fire = False
move_right = False
move_left = False

alien_fired = False
player_died = False


shoot_sound = pygame.mixer.Sound("shoot.wav")
alien_killed_sound = pygame.mixer.Sound("alienkilled.wav")
death = pygame.mixer.Sound("explosion.wav")

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")

class Lives():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        life = pygame.image.load("ship.png")
        screen.blit(life,(self.x,self.y))

life1 = Lives(10,560)
life2 = Lives(60,560)
life3 = Lives(110,560)

lives = [life1,life2,life3]

class player_ship():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 5
        
    def draw(self):
        ship = pygame.image.load("ship.png")
        screen.blit(ship,(self.x,self.y))

    def move_right(self):
        self.x += self.vel
        
        if self.x >= 550:
            self.x = 560
    
    def move_left(self):
        self.x -= self.vel

        if self.x < 0:
            self.x = 0

char = player_ship(200,530)


class Alien1():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 1
        self.hit = False

    def draw(self):
        if self.hit == False:
            alien1 = pygame.image.load("alien1.png")
            screen.blit(alien1, (self.x,self.y))

    def alien_last_move(self):
        self.x += self.vel

        if self.x >= WIDTH-40:
            for i in aliens:
                i.y += 10
                i.vel *= -1
            for i in aliens3:
                i.y += 10
                i.vel *= -1

            
    def alien_first_move(self):
        self.x += self.vel
        
        if self.x <= 0:
            for i in aliens:
                i.y += 10
                i.vel *= -1

            for i in aliens3:
                i.y += 10
                i.vel *= -1

    def move(self):
        self.x += self.vel
    

    def shot(self):
        if self.hit == False:
            if bullet_x >= self.x and bullet_x <= self.x + 40 and bullet_y >= self.y and bullet_y <= self.y + 40:
                self.hit = True
                shot = pygame.image.load("explosion.png")
                screen.blit(shot,(self.x,self.y))
                pygame.mixer.Sound.play(alien_killed_sound)
                return True

    def check_invade(self):
        if alien1.y == 60:
            self.vel = 2
        if self.y >= 530:
            lives = []
            pygame.QUIT

alien1 = Alien1(50,0)
alien2 = Alien1(100,0)
alien3 = Alien1(150,0)
alien4 = Alien1(200,0)
alien5 = Alien1(250,0)
alien6 = Alien1(300,0)
alien7 = Alien1(350,0)
alien8 = Alien1(400,0)
alien9 = Alien1(450,0)
alien10 = Alien1(500,0)


alien3_1 = Alien1(50,60)
alien3_2 = Alien1(100,60)
alien3_3 = Alien1(150,60)
alien3_4 = Alien1(200,60)
alien3_5 = Alien1(250,60)
alien3_6 = Alien1(300,60)
alien3_7 = Alien1(350,60)
alien3_8 = Alien1(400,60)
alien3_9 = Alien1(450,60)
alien3_10 = Alien1(500,60)


class Alien2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 1
        self.hit = False

    def draw(self):
        if self.hit == False:
            alien2 = pygame.image.load("alien2.png")
            screen.blit(alien2, (self.x,self.y))

    def alien_last_move(self):
        self.x += self.vel

        if self.x >= WIDTH-40:
            for i in aliens2:
                i.y += 10
                i.vel *= -1

            for i in aliens4:
                i.y += 10
                i.vel *= -1

            
    def alien_first_move(self):
        self.x += self.vel
        
        if self.x <= 0:
            for i in aliens2:
                i.y += 10
                i.vel *= -1

            for i in aliens4:
                i.y += 10
                i.vel *= -1

    def move(self):
        self.x += self.vel

    def shot(self):
        if self.hit == False:
            if bullet_x >= self.x and bullet_x <= self.x + 40 and bullet_y >= self.y and bullet_y <= self.y + 40:
                self.hit = True
                shot = pygame.image.load("explosion.png")
                screen.blit(shot,(self.x,self.y))
                pygame.mixer.Sound.play(alien_killed_sound)
                return True

    def check_invade(self):
        if alien2_1.y == 90:
            self.vel = 2
            
        if self.y >= 530:
            lives = []
            pygame.QUIT


alien2_1 = Alien2(50,30)
alien2_2 = Alien2(100,30)
alien2_3 = Alien2(150,30)
alien2_4 = Alien2(200,30)
alien2_5 = Alien2(250,30)
alien2_6 = Alien2(300,30)
alien2_7 = Alien2(350,30)
alien2_8 = Alien2(400,30)
alien2_9 = Alien2(450,30)
alien2_10 = Alien2(500,30)

alien4_1 = Alien2(50,90)
alien4_2 = Alien2(100,90)
alien4_3 = Alien2(150,90)
alien4_4 = Alien2(200,90)
alien4_5 = Alien2(250,90)
alien4_6 = Alien2(300,90)
alien4_7 = Alien2(350,90)
alien4_8 = Alien2(400,90)
alien4_9 = Alien2(450,90)
alien4_10 = Alien2(500,90)

 

bullet_x = char.x + 15
bullet_y = char.y

aliens = [alien1,alien2,alien3,alien4,alien5,alien6,alien7,alien8,alien9,alien10]

aliens2 = [alien2_1,alien2_2,alien2_3,alien2_4,alien2_5,alien2_6,alien2_7,alien2_8,alien2_9,alien2_10]

aliens3 = [alien3_1,alien3_2,alien3_3,alien3_4,alien3_5,alien3_6,alien3_7,alien3_8,alien3_9,alien3_10]

aliens4 = [alien4_1,alien4_2,alien4_3,alien4_4,alien4_5,alien4_6,alien4_7,alien4_8,alien4_9,alien4_10]

list_alien = [aliens,aliens2,aliens3,aliens4]

running = True

while running:
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_SPACE:
                if fire == False:
                    bullet_x = char.x + 20
                    bullet_y = char.y
                    fire = True
                    pygame.mixer.Sound.play(shoot_sound)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right == True:
        char.move_right()

    if move_left == True:
        char.move_left()
        
    if fire == True:
        pygame.draw.rect(screen,GREEN ,(bullet_x,bullet_y,5,10))
        bullet_y -= 10

        if bullet_y < 0:
            fire = False


    if alien_fired == False:
        shooter_alien = random.choice(list_alien)

        if shooter_alien == aliens:
            shooter = random.choice(aliens)
            if shooter.hit == False:
                alien_bulletx = shooter.x + 20
                alien_bullety = shooter.y + 20
                alien_fired = True

        if shooter_alien == aliens2:
            shooter = random.choice(aliens2)
            if shooter.hit == False:
                alien_bulletx = shooter.x + 20
                alien_bullety = shooter.y + 20
                alien_fired = True

        if shooter_alien == aliens3:
            shooter = random.choice(aliens3)
            if shooter.hit == False:
                alien_bulletx = shooter.x + 20
                alien_bullety = shooter.y + 20
                alien_fired = True

        if shooter_alien == aliens4:
            shooter = random.choice(aliens4)
            if shooter.hit == False:
                alien_bulletx = shooter.x + 20
                alien_bullety = shooter.y + 20
                alien_fired = True
    

    if alien_fired == True:
        pygame.draw.rect(screen,RED, (alien_bulletx,alien_bullety,5,10))
        alien_bullety += 10
        if alien_bulletx >= char.x and alien_bulletx <= char.x + 40 and alien_bullety == char.y+10:
            lives.pop()
            pygame.mixer.Sound.play(death)

        if alien_bullety >= HEIGHT:
            alien_fired = False


                
    for i in aliens:
        if i.shot():
            bullet_x = char.x + 15
            bullet_y = char.y
            pygame.draw.rect(screen,WHITE,(bullet_x,bullet_y,5,10))
            fire = False
            
    for i in aliens2:
        if i.shot():
            bullet_x = char.x + 15
            bullet_y = char.y
            pygame.draw.rect(screen,WHITE,(bullet_x,bullet_y,5,10))
            fire = False
    
    for i in aliens3:
        if i.shot():
            bullet_x = char.x + 15
            bullet_y = char.y
            pygame.draw.rect(screen,WHITE,(bullet_x,bullet_y,5,10))
            fire = False

    for i in aliens4:
        if i.shot():
            bullet_x = char.x + 15
            bullet_y = char.y
            pygame.draw.rect(screen,WHITE,(bullet_x,bullet_y,5,10))
            fire = False
            
    if player_died == False:
        char.draw()
        
    for i in aliens:
        if i != alien1 and i != alien10:
            i.draw()
            i.shot()
            i.move()
            i.check_invade()

        if i == alien1:
            i.alien_first_move()
            i.draw()
            i.shot()
            i.check_invade()
        if i == alien10:
            i.alien_last_move()
            i.draw()
            i.shot()
            i.check_invade()

    for i in aliens2:
        if i != alien2_1 and i != alien2_10:
            i.draw()
            i.shot()
            i.move()
            i.check_invade()
        
        if i == alien2_1:
            i.alien_first_move()
            i.draw()
            i.shot()
            i.check_invade()

        if i == alien2_10:
            i.alien_last_move()
            i.draw()
            i.shot()
            i.check_invade()
    
    for i in aliens3:
        if i != alien3_1 and i != alien3_10:
            i.draw()
            i.shot()
            i.move()
            i.check_invade()
        
        if i == alien3_1:
            i.alien_first_move()
            i.draw()
            i.shot()
            i.check_invade()

        if i == alien3_10:
            i.alien_last_move()
            i.draw()
            i.shot()
            i.check_invade()

    for i in aliens4:
        if i != alien4_1 and i != alien4_10:
            i.draw()
            i.shot()
            i.move()
            i.check_invade()
        
        if i == alien4_1:
            i.alien_first_move()
            i.draw()
            i.shot()
            i.check_invade()

        if i == alien4_10:
            i.alien_last_move()
            i.draw()
            i.shot()
            i.check_invade()

    for i in lives:
        i.draw()

    if len(lives) == 0:
        player_died = True
        explosion = pygame.image.load("playerexplosion.png")
        screen.blit(explosion,(char.x,char.y))
        pygame.mixer.Sound.play(death)
        lives.append(1)
       
        
    pygame.display.update()
