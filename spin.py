import pygame
pygame.init()

WIDTH=1000
HEIGHT=600
TITLE="SPACE INVADERS"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
go=False
rbullets=[]
ybullets=[]
YHealth=100
RHealth=100

bg1=pygame.image.load("Yship.png")
bg2=pygame.image.load("Wbg.png")
bg3=pygame.image.load("Rship.png")
bg4=pygame.image.load("bullet.png")
bg1=pygame.transform.scale(bg1,(75,75))
bg3=pygame.transform.scale(bg3,(75,75))

class Ships(pygame.sprite.Sprite):
  def __init__(self,x,y,image,angle):
    super().__init__()
    self.image=pygame.transform.rotate(image,angle)
    self.rect=self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
  def move(self,player,vx,vy):
    self.rect.x+=vx
    self.rect.y+=vy
    if self.rect.top<0:
        self.rect.top=0
    if self.rect.bottom>600:
        self.rect.bottom=600
    if player==1:  
      if self.rect.left<0:
          self.rect.left=0
      if self.rect.right>500:
          self.rect.right=500
    if player==2:  
      if self.rect.left<500:
          self.rect.left=500
      if self.rect.right>1000:
          self.rect.right=1000  

yship=Ships(250,300,bg1,90)
rship=Ships(750,300,bg3,270)
players=pygame.sprite.Group()
players.add(yship)
players.add(rship)

def handlebullets():
  global RHealth,YHealth
  for bullet in ybullets:
    pygame.draw.rect(screen,"White",bullet,0)
    bullet.x=bullet.x+10
    if bullet.colliderect(rship.rect):
      RHealth=RHealth-10
      ybullets.remove(bullet)
  for bullet in rbullets:
    pygame.draw.rect(screen,"White",bullet,0)   
    bullet.x=bullet.x-10
    if bullet.colliderect(yship.rect):
      YHealth=YHealth-10
      rbullets.remove(bullet)
      
    

while go==False:
  screen.blit(bg2,(0,0))
  players.draw(screen)
  font=pygame.font.SysFont("comic sans",50)
  message1=font.render("YHealth = " + str(YHealth),True,"WHITE")
  message2=font.render("RHealth = " + str(RHealth),True,"WHITE") 
  screen.blit(message1,(0,0))
  screen.blit(message2,(750,0))
  handlebullets()
  pygame.draw.line(screen,"Black",(500,0),(500,600),20)
  ks=pygame.key.get_pressed()
  if ks[pygame.K_w]:
    yship.move(1,0,-2)
  if ks[pygame.K_s]:
    yship.move(1,0,2)
  if ks[pygame.K_d]:
    yship.move(1,2,0)
  if ks[pygame.K_a]:
    yship.move(1,-2,0)
  if ks[pygame.K_UP]:
    rship.move(2,0,-2)
  if ks[pygame.K_DOWN]:
    rship.move(2,0,2)
  if ks[pygame.K_RIGHT]:
    rship.move(2,2,0)
  if ks[pygame.K_LEFT]:
    rship.move(2,-2,0) 
  
  for event in pygame.event.get(): 
    if event.type==pygame.QUIT:
      go=True 
    if event.type==pygame.MOUSEBUTTONDOWN:
      bullet=pygame.Rect(rship.rect.x-15,rship.rect.y+35,30,5)
      rbullets.append(bullet)
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_SPACE: 
        bullet=pygame.Rect(yship.rect.x+60,yship.rect.y+35,30,5)      
        ybullets.append(bullet)
  if YHealth==0:
    message3=font.render("Press Y to restart the game, N to quit",True,"WHITE")
    for event in pygame.event.get(): 
      if event.type==pygame.K_y:
        YHealth=100
        RHealth=100
      if event.type==pygame.K_n:
        go=True
    screen.blit(message3,(500,300))         
  if RHealth==0:
    message4=font.render("Press Y to restart the game, N to quit",True,"WHITE")    
    for event in pygame.event.get(): 
      if event.type==pygame.K_y:
        YHealth=100
        RHealth=100
      if event.type==pygame.K_n:
        go=True
      else:
        YHealth=100
        RHealth=100
    screen.blit(message4,(500,300))  
  pygame.display.update()