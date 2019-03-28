import pygame,sys
from settings import *

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.sceen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state ='start'
    def run(self):
        while self.running:
            if self.state == 'start':
                self.state_events()
                self.state_update()
                self.state_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

#######################Help##################################
    def draw_text(self,words,screen,pos,size,color,font_name,center = False):
        font = pygame.font.SysFont(font_name,size,)
        text = font.render(words, False,color)
        text_size = text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text,pos)
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
        self.sceen.fill(BLACK)  #Background color
        self.draw_text('Press Space Bar',self.sceen,[WIDTH//2,HEIGHT//2],
                        START_TEXT_SIZE,(170,132,58),START_FONT)
        pygame.display.update()