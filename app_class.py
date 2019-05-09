import pygame,sys
from settings import *
from player_class import *
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state ='start'

        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30

        self.player = Player(self,PLAYER_START_POS)
        self.walls =[]
        self.coins =[]
        self.load()   #Load board
    def run(self):
        while self.running:
            if self.state == 'start':
                self.state_events()
                self.state_update()
                self.state_draw()

            if self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


    def draw_text(self,words,screen,pos,size,color,font_name,center = False):
        font = pygame.font.SysFont(font_name,size,)
        text = font.render(words, False,color)
        text_size = text.get_size()
        if center:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text,pos)


    def load(self):
        self.background = pygame.image.load('board.png')
        self.background = pygame.transform.scale(self.background,(MAZE_WIDTH,MAZE_HEIGHT))
        #open file wall and create wall liist with x and y of wall
        with open("wall.txt",'r') as file: ###Scale the image
            for yidx ,line in enumerate(file):
                for xidx,char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx,yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
        #print(self.walls)

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):#Draw vertical line from left to right
            pygame.draw.line(self.background,GREY,(x*self.cell_width,0),(x*self.cell_width,HEIGHT))

        for x in range(HEIGHT//self.cell_height):#Draw horizontal line from top to bottom
            pygame.draw.line(self.background,GREY,(0,x*self.cell_height),(WIDTH,x*self.cell_height))

        #draw whare the coin position
        for coin in self.coins:
            pygame.draw.rect(self.background,(167,180,34),
                             (coin.x*self.cell_width,coin.y*self.cell_height,self.cell_width,self.cell_height))


#######################Intro##################################

    def state_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'


    def state_update(self):
        pass
    def state_draw(self):
        self.screen.fill(BLACK)  #Background color
        #######Menu#####
        self.draw_text('Press Space Bar',self.screen,[WIDTH//2,HEIGHT//2],
                        START_TEXT_SIZE,(170,132,58),START_FONT,center= True)
        self.draw_text('1 Player', self.screen, [WIDTH // 2, HEIGHT // 2+35],
                       START_TEXT_SIZE, (33,137,156), START_FONT,center= True)
        self.draw_text('High Score', self.screen, [0,0],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()

######################Play###############

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0,1))

    def playing_update(self):
        self.player.update()
    def playing_draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.background,
                         (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))  #Display sceen with space top bottom left and right
        self.draw_coins()
        # self.draw_grid()
        #pass the score in integer to the current score on the board
        self.draw_text('Current Score: {}'.format(self.player.current_score),self.screen,[10,0],18,WHITE,START_FONT)
        self.draw_text('High Score: 0', self.screen, [WIDTH//2, 0], 18, WHITE, START_FONT)
        self.player.draw()
        pygame.display.update()
         #when pacman eat, coin will disappear

    def draw_coins(self):
        for coin in self.coins:  #draw coin with background and position with radius 5
            pygame.draw.circle(self.screen,(82,200,150),
                            (int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2, #+self.cell_width//2 for the coin in the center of lin
                            int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2),5)