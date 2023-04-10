
import pygame  
pygame.init()
screen = pygame.display.set_mode((400, 400))
mickey = pygame.image.load("Week9/lab07/Clock/mickeymouse.png")
left = pygame.image.load("Week9/lab07/Clock/LeftHand.png")
right = pygame.image.load("Week9/lab07/Clock/Righthand.png")
def blitRotateCenter(surf, image, center, angle):
    rotatedImage = pygame.transform.rotate(image, angle)
    new_rect = rotatedImage.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotatedImage, new_rect)
langle = 0
rangle = 0

running = True
while running:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    langle -= 2
    rangle -= 1
    screen.fill("white")
    screen.blit(mickey, (200, 200))
    screen.blit(mickey, mickey.get_rect())

    blitRotateCenter(screen, left, (200, 200), langle)
    blitRotateCenter(screen, right, (200, 200), rangle)
    clock = pygame.time.Clock()
    clock.tick(5)
 