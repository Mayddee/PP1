import pygame
pygame.init()
scr = pygame.display.set_mode((700, 500))
pygame.display.set_caption("moving ball")

vel = 20
x = 25
y = 25

running = True
while running:
    scr.fill("WHITE")
    crcl = pygame.draw.circle(scr, "RED", (x, y), 25)
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
              if x > 670:
                x += 0
              else:
                x += vel
            elif event.key == pygame.K_LEFT:
              if x < 30:
                x -= 0
              else:
                x -= vel
            elif event.key == pygame.K_DOWN:
              if y > 470:
                y += 0
              else:
                y += vel
            elif event.key == pygame.K_UP:
              if y < 30:
                y -= 0
              else:
                y -= vel
    