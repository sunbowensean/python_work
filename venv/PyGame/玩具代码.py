import pygame
pygame.init()

w,h = 500,500
pygame.display.set_mode((w,h))
screen = pygame.display.get_surface()

#载入背景图且缩放宽高
bgpic = pygame.image.load('bgpic.png')
bgpic = pygame.transform.scale(bgpic(w,h))
#载入角色图
mario_image = pygame.image.load('Mario.png')

#创建精灵
mario = pygame.sprite.Sprite()
mario.image = mario_image
mario.rect = mario.image.get_rect()
mario.rect.x,mario.rect.y = w/2,h/2

#玩家组
player_group = pygame.sprite.Group()
player_group.add(mario)

#start game
while True:
    #更新
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        if event == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                mario.rect.y += 10
            if keys[pygame.K_RIGHT]:
                mario.rect.y -= 10
    #draw
    screen.blit(bgpic,(0,0))
    player_group.draw(screen)
    pygame.display.update()
