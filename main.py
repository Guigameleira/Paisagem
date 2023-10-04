import pygame
width = 800
height = 600
running = True
x_nuvem= 500
nuvem_esquerda=True
y_sol=70


def load():
  global clock, minha_imagem
  clock = pygame.time.Clock() 
  minha_imagem = pygame.image.load("image.png")
  minha_imagem = pygame.transform.scale (minha_imagem, (100, 150))

#som
pygame.mixer.init()
pygame.mixer.music.load("hino flu.mp3")
pygame.mixer.music.play()


def draw_screen(screen, x_nuvem, ):
  pygame.draw.rect(screen,(0,200,255),(0,0,800,600))
  if y_sol> 200 and y_sol<=210:
    pygame.draw.rect(screen,(48,199, 230), (0,0,800,600))
  if y_sol> 210 and y_sol<=220:
    pygame.draw.rect(screen,(2, 158, 247), (0,0,800,600))
  if y_sol> 220 and y_sol<=230:
    pygame.draw.rect(screen,(7, 94, 181), (0,0,800,600))
  if y_sol> 230 and y_sol<=245:
    pygame.draw.rect(screen,(28, 40, 140), (0,0,800,600))
  if y_sol> 245:
    pygame.draw.rect(screen,(6, 9 , 112), (0,0,800,600))
  #sol
  pygame.draw.circle(screen,(255, 255, 0),( 90,y_sol), 35)
  pygame.draw.lines(screen, (255,255,0), False, [(30, y_sol - 20), (150, y_sol +30)], 3)
  pygame.draw.lines(screen, (255,255,0), False, [(30, y_sol + 30), (150, y_sol - 20)], 3)
  pygame.draw.lines(screen, (255,255,0), False, [(90, y_sol - 65), (90,y_sol+ 55)], 3)
  pygame.draw.rect(screen,(0, 134, 0),(0, 300, 800,500))
  #casa
  pygame.draw.rect(screen,(105, 104, 102),(125, 175, 125,125))
  pygame.draw.polygon(screen,(250, 2, 19),[(125, 175),(187, 80),(250, 175)])
  pygame.draw.rect(screen,(99, 40, 14),(187, 220, 40,80))
  pygame.draw.circle(screen,(0,0,0),(195,255), 4)
  pygame.draw.rect(screen,(16, 33, 222),(140,200,30,40))
  #arvore
  pygame.draw.rect(screen,(48, 21, 4),(450,200,30,100))
  pygame.draw.circle(screen,(10, 250, 58),(460,180), 55)
  
  for i in range(4):
    pygame.draw.circle(screen,(255, 255, 255),(x_nuvem,50), 25)
    x_nuvem+=45
  screen.blit(minha_imagem, (550, 200))

def update(dt):
  global x_nuvem , nuvem_esquerda, y_sol
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
      y_sol=y_sol - (0.1*dt)
  if keys[pygame.K_DOWN]:
      y_sol=y_sol + (0.1*dt)  
  if y_sol > 340:
     y_sol= 340
  if y_sol < 0:
     y_sol=0
  
  if nuvem_esquerda:
    if x_nuvem  < 0:
      nuvem_esquerda = False
    x_nuvem = x_nuvem - (0.1 * dt)
  else:
    if x_nuvem  > width:
      nuvem_esquerda = True 
    x_nuvem = x_nuvem + (0.1 * dt)
  
def main_loop(screen):
  while running:
    for e in pygame.event.get():
      if e .type == pygame.QUIT:
        running == False
    clock.tick(60)
        
    dt = clock.get_time()
    draw_screen(screen, x_nuvem)
    update(dt)
    pygame.display.update()
    

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)

pygame.quit()
