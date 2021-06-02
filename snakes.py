
import pygame
import random

#define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('bg.mp3')
pygame.mixer.music.play()


screen_width = 800
screen_length = 600
gameWindow = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("Snakes")
pygame.display.update()


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size,snake_size])


def gameloop():
    prevkey1 = pygame.K_UP
    prevkey2 = pygame.K_0
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 30
    vel=5
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(200,600)
    food_y = random.randint(100,500)
    snake_list = []
    snake_length = 1
    
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen(f'Game Over! Score: {score}', red, 200, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('bg.mp3')
                        pygame.mixer.music.play()
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT and (prevkey1==pygame.K_UP or prevkey1==pygame.K_DOWN):
                        prevkey1 = pygame.K_RIGHT
                        velocity_x=vel
                        velocity_y=0

                    if event.key == pygame.K_LEFT and (prevkey1==pygame.K_UP or prevkey1==pygame.K_DOWN):
                        prevkey1 = pygame.K_LEFT
                        velocity_x=-vel
                        velocity_y=0

                    if event.key == pygame.K_UP and (prevkey1==pygame.K_LEFT or prevkey1==pygame.K_RIGHT):
                        prevkey1 = pygame.K_UP
                        velocity_x=0
                        velocity_y=-vel

                    if event.key == pygame.K_DOWN and (prevkey1==pygame.K_LEFT or prevkey1==pygame.K_RIGHT):
                        prevkey1 = pygame.K_DOWN
                        velocity_x=0
                        velocity_y=vel

            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=1
                # print(score)
                food_x = random.randint(200,600)
                food_y = random.randint(100,500)
                vel+=0.25
                snake_length+=2


            gameWindow.fill(white)
            text_screen('Score: ' + str(score), red, 5, 5)
            pygame.draw.circle(gameWindow, red, [food_x, food_y], 5)
            #Snake Head
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_length:
                game_over = True
            
            plot_snake(gameWindow, green, snake_list, snake_size)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()
