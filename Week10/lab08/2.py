from pygame.locals import *
import pygame, sys
import random, time

BLACK = (0, 0, 0)
#YELLOW= (238,255,27)
#GREY = (50, 50, 50)
#BLUE  = (0, 0, 255)
#RED   = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

HEIGHT = 495
WIDTH = 405

BLOCK_SIZE = 15

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food:
    def __init__(self):
        #food appears randomly
        self.location = Point(random.randint(1, 20), random.randint(1, 20))

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 127), rect)


class Snake:
    def __init__(self):
        self.body = [Point(5, 5)]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        global game
        game = True

        #liminates by borders for moving
        if self.body[0].x * BLOCK_SIZE > WIDTH:
            game = False
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            game = False

        if self.body[0].x < 0:
            game = False

        if self.body[0].y < 0:
            game = False

    def draw(self):
        #draws head
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 204, 0), rect)

        #draws body
        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    #checks weather the snake and food collide or not, if they do appends a part to the body
    def check_collision(self, food):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                
                #changes the location of food after collision
                food.location = Point(random.randint(1, WIDTH // BLOCK_SIZE - 1), random.randint(1, HEIGHT // BLOCK_SIZE - 1))


def main():
    global SCREEN, CLOCK, FPS, score, speed
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Snake")

    font_ = pygame.font.SysFont("VERDANA", 30)
    game_over = font_.render("GAME OVER", True, BLACK)
    font_text = pygame.font.SysFont("VERDANA", 15)
    
    
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    FPS = 5
    level = ["easy", "normal", "hard", "very hard", "demanding", "impossible"]
    score = 0
    speed = 1

    snake = Snake()
    food = Food()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
        
        snake.move()

        #increases speed when the snake eats 4 times
        speed = score//4 + 1

        #closes the screen after a collision
        if game == False:
            time.sleep(0.5)
            SCREEN.fill(WHITE)
            SCREEN.blit(game_over, (100, 170))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        #checks whether the snake and food collide or not, if they do appends a part to the body
        if snake.body[0].y == food.location.y:
            if snake.body[0].x == food.location.x:
                score += 1
                snake.body.append(Point(food.location.x, food.location.y))
                
                #changes the location of food after collision
                food.location = Point(random.randint(1, WIDTH // BLOCK_SIZE - 1), random.randint(1, HEIGHT // BLOCK_SIZE - 1))
        
        
        SCREEN.fill((204, 255, 153))
        snake.draw()
        food.draw()

        scores = font_text.render(f"Scores: {score}", True, BLACK)
        
        if score < 100:
            levels = font_text.render(f"Level: {level[score//4]}", True, BLACK)
        else:
            levels = font_text.render(f"Level: {level[5]}", True, BLACK)
        SCREEN.blit(scores, (10, 10))
        
        SCREEN.blit(levels, (240, 10))

        
        snake.draw()
        food.draw()

        pygame.display.update()
        
        CLOCK.tick(FPS + speed)

main()