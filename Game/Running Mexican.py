# Import a library of functions called 'pygame'

import pygame
import time

# define display surface
displayWidth = 892
displayHeight = 400

# initialise display
pygame.init()
jump_sound = pygame.mixer.Sound("jump.wav")
scream_sound = pygame.mixer.Sound("screaming.wav")
pygame.mixer.music.load("music.wav")
pygame.mixer.music.set_volume(0.05)
scream_sound.set_volume(0.3)
jump_sound.set_volume(0.3)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([displayWidth, displayHeight])
pygame.display.set_caption("Running Mexican")
intro = True
done = False
gameOver = False
winner = False
frame_count = 0
start_time = 15

"Graphics---------------------------------------------------------"
BLACK = (0,0,0)
WHITE = (255,255,255)
GROUND = (139,69,19)
RED = (200,0,0)
BRED = (255,0,0)
GREEN = (0,200,0)
BGREEN =(0,255,0)
DESSERT = pygame.image.load('Desert.png')
DESSERTX = 0
heroImg = pygame.image.load('hero.png')
cactusImg = pygame.image.load('cactus.png')
"------------------------------------------------------------------"
def intro_screen():
    while intro == True:
        screen_picture()
        button("Start", displayWidth/2-75, displayHeight/2-50, 150, 100, GREEN, BGREEN, "introplay")
        exit()
        pygame.display.flip()
        clock.tick(50)

def exit():
    global done, gameOver,intro, winner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
            done = True
            gameOver = False
            winner = False

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('comic.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayWidth/2),(displayHeight/2))
    screen.blit(TextSurf, TextRect)

def screen_picture():
    screen.fill(WHITE)
    screen.blit(DESSERT, (DESSERTX, 0))
    pygame.draw.line(screen, GROUND, [0, displayHeight - 20], [displayWidth, displayHeight - 20], 20)

def theEnd():
    global distanceX, distanceY, gameOver
    distanceX1 = C1.x - P.x
    distanceX2 = C2.x-P.x
    distanceX3 = C3.x - P.x
    distanceY = C1.y - P.y
    if (distanceX1 < 35 and distanceX1 > -35 and distanceY < 40) or (distanceX2 < 35 and distanceX2 > -35 and distanceY < 40)or (distanceX3 < 35 and distanceX3 > -35 and distanceY < 40):
        pygame.draw.line(screen, RED, [0, displayHeight - 20], [displayWidth, displayHeight - 20], 20)
        pygame.mixer.Sound.play(scream_sound)
        gameOver = True

def button (text,x,y,w,h,color, acolor,action) :
    global gameOver, done, intro, C1,C2,C3, frame_count,winner
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + 150 > mouse[0] > x and y + 100 > mouse[1] > y:
        pygame.draw.rect(screen, acolor, (x, y, w, h))
        if click[0] == 1:
            if action == "quit":
                winner = False
                gameOver = False
                done = True
            elif action == "introplay":
                intro =False
            elif action == "play":
                gameOver = False
                winner = False
                frame_count = 0
                pygame.mixer.music.play(-1)
                C1 = Cactus(300, displayHeight - 10)
                C2 = Cactus(800, displayHeight - 10)
                C3 = Cactus(1000, displayHeight - 10)
                P.setLocation(20, displayHeight - 10)
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))
    smallText = pygame.font.Font('comic.ttf', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(TextSurf, TextRect)

def gameOverScreen():
    while gameOver:
        pygame.mixer.music.stop()
        screen_picture()
        message_display('Cactus burns you')
        button("Quit",50,20,150,100,RED,BRED,"quit")
        button("Try it again",692,20,150,100,GREEN,BGREEN,"play")
        exit()
        pygame.display.flip()
        clock.tick(50)

def winnerScreen():
    while winner:
        pygame.mixer.music.stop()
        screen_picture()
        message_display('You win a tequila')
        button("Quit",50,20,150,100,RED,BRED,"quit")
        button("Try it again",692,20,150,100,GREEN,BGREEN,"play")
        exit()
        pygame.display.flip()
        clock.tick(50)



def timer():
    global frame_count, gameOver, winner
    smallText = pygame.font.Font('comic.ttf', 20)
    total_seconds = start_time - (frame_count / 60)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds / 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = smallText.render(output_string, True, BLACK)
    screen.blit(text, [displayWidth-170, 20])
    frame_count += 1
    if seconds <= 0:
        winner = True
        winnerScreen()
"--------------------Cactus----------------------------------------"
class Cactus():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(cactusImg, (self.x, displayHeight - 80))

    def move(self):
        self.x = self.x - 2
        if self.x < 0 :
            self.x = displayWidth

    def do(self):
        self.draw()
        self.move()

"---------------------END CACTUS------------------------------------"
"----------------------Player---------------------------------------"
class Player ():
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange

    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True


    def keys(self):
        k = pygame.key.get_pressed()

        if k[pygame.K_LEFT]:
            self.xVelocity = -self.velocity
        elif k[pygame.K_RIGHT]:
            self.xVelocity = self.velocity
        else:
            self.xVelocity = 0

        if k[pygame.K_UP] and not self.jumping and not self.falling:
            pygame.mixer.Sound.play(jump_sound)
            self.jumping = True
            self.jumpCounter = 0



    def move(self):
        self.x += self.xVelocity


        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y <= displayHeight - 10 and self.y + self.velocity >= displayHeight - 10:
                self.y = displayHeight - 10
                self.falling = False
            else:
                self.y += self.velocity


    def draw(self):
        display = pygame.display.get_surface()
        #pygame.draw.circle(display, WHITE, (self.x, self.y - 25), 25, 0)
        screen.blit(heroImg, (self.x, self.y - 80))

    def do(self):
        self.keys()
        self.move()
        self.draw()

"----------------------END PLAYER-----------------------------------"
C1 = Cactus(300,displayHeight-10)
C2 = Cactus(800,displayHeight-10)
C3 = Cactus(1000,displayHeight-10)
P = Player(2, 50)
P.setLocation(20,displayHeight-10)

pygame.mixer.music.play(-1)
intro_screen()
while not done:
    screen_picture()
    timer()
    C1.do()
    C2.do()
    C3.do()
    P.do()
    theEnd()
    gameOverScreen()
    winnerScreen()
    exit()
    pygame.display.flip()
    clock.tick(60)
