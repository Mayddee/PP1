import pygame
pygame.init()
#clock = pygame.time.Clock()
scr = pygame.display.set_mode((549, 363))
img = pygame.image.load("C:\pp2 0\Pygame\images\BTS0.jpg")
name = pygame.display.set_caption("BTS Music Player")
mp = [r"Week9/lab07/Musics/BTS - Airplane pt.2.mp3",
      r"Week9/lab07/Musics/BTS - Black Swan.mp3",
      r"Week9/lab07/Musics/BTS - DNA.mp3",
      r"Week9/lab07/Musics/BTS - FAKE LOVE.mp3",
      r"Week9/lab07/Musics/BTS - Butter.mp3"]
i = 0
pygame.mixer.music.load(mp[0])
pygame.mixer.music.play()

running = True
mcpause = False
while running:
    scr.blit(img, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mcpause = not mcpause
                if mcpause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
             if i < 0 or i > 3:
                i += 0
             else:
                i += 1
                pygame.mixer.music.load(mp[i])
                pygame.mixer.music.play()
                
                
            elif event.key == pygame.K_LEFT:
             if i < 1 or i > 4:
                i -= 0
             else:
                i -= 1
                pygame.mixer.music.load(mp[i])
                pygame.mixer.music.play()
                
            elif event.key == pygame.K_LSHIFT:
                pygame.mixer.music.stop()
            
    #pygame.clock.tick(60)

    