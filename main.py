import os
import pygame
import sys
import random

pygame.init()

#property
width = 1500
height = 900

end_font = pygame.font.SysFont("Gotham", 100)
score_font = pygame.font.SysFont("Gotham", 40)

eat_sound = pygame.mixer.Sound(os.path.join("sounds", "eat.wav"))
pygame.mixer.music.load(os.path.join("sounds", "sound_background.mp3"))

player_size_update = 0
player_size = [110, 110]
player_position = [width/2-player_size[0], height/2-player_size[1]]
direction = "left"

#status game
gameOver = False
status = "lost"

# enemy property
enemy1_image = pygame.image.load(os.path.join("images", "enemy1.png"))
enemy2_image = pygame.image.load(os.path.join("images", "enemy2.png"))
enemy3_image = pygame.image.load(os.path.join("images", "enemy3.png"))
enemy4_image = pygame.image.load(os.path.join("images", "enemy4.png"))

enemy1_image = pygame.transform.scale(enemy1_image, (100, 100))
enemy2_image = pygame.transform.scale(enemy2_image, (270, 270))
enemy3_image = pygame.transform.scale(enemy3_image, (140, 140))
enemy4_image = pygame.transform.scale(enemy4_image, (200, 200))

enemy1_position = [0, random.sample(range(0, height), 1)[0]]
enemy2_position = [0, random.sample(range(0, height), 1)[0]]
enemy3_position = [0, random.sample(range(0, height), 1)[0]]
enemy4_position = [0, random.sample(range(0, height), 1)[0]]

enemy1_size = [90, 90]
enemy2_size = [250, 250]
enemy3_size = [140, 140]
enemy4_size = [200, 200]

enemy1_speed = 5
enemy2_speed = 15
enemy3_speed = 7
enemy4_speed = 10

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

#background
background = pygame.image.load(os.path.join("images", "background.jpg"))
background = pygame.transform.scale(background, (width, height))

background_endgame = pygame.image.load(os.path.join("images/end_game", "end.jpg"))
background_endgame = pygame.transform.scale(background_endgame, (width, height))

background_wingame = pygame.image.load(os.path.join("images", "background_win.jpg"))
background_wingame = pygame.transform.scale(background_wingame, (width, height))

count_bubble = 0

pygame.display.set_caption('FISH GAME')

def enemy1_crash(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]
    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size[0])) or (p_x >= e_x and p_x < (e_x+enemy1_size[0])):
        if (e_y >= p_y and e_y < (p_y + player_size[1])) or (p_y >= e_y and p_y < (e_y + enemy1_size[1])):
            return True
    return False

def enemy2_crash(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]
    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size[0])) or (p_x >= e_x and p_x < (e_x+enemy2_size[0])):
        if (e_y >= p_y and e_y < (p_y + player_size[1])) or (p_y >= e_y and p_y < (e_y + enemy2_size[1])):
            return True
    return False

def enemy3_crash(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]
    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size[0])) or (p_x >= e_x and p_x < (e_x+enemy3_size[0])):
        if (e_y >= p_y and e_y < (p_y + player_size[1])) or (p_y >= e_y and p_y < (e_y + enemy3_size[1])):
            return True
    return False

def enemy4_crash(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]
    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size[0])) or (p_x >= e_x and p_x < (e_x+enemy4_size[0])):
        if (e_y >= p_y and e_y < (p_y + player_size[1])) or (p_y >= e_y and p_y < (e_y + enemy4_size[1])):
            return True
    return False

def enemy_move():
    if enemy1_position[0] >= 0 and enemy1_position[0] < width:
        enemy1_position[0] += enemy1_speed
    else:
        enemy1_position[1] = random.randint(0, height-enemy1_size[0])
        enemy1_position[0] = 0

    if enemy2_position[0] >= 0 and enemy2_position[0] <= width:
        enemy2_position[0] -= enemy2_speed
    else:
        enemy2_position[1] = random.randint(0, height-enemy2_size[0])
        enemy2_position[0] = width

    if enemy3_position[0] >= 0 and enemy3_position[0] <= width:
        enemy3_position[0] -= enemy3_speed
    else:
        enemy3_position[1] = random.randint(0, height-enemy3_size[0])
        enemy3_position[0] = width

    if enemy4_position[0] >= 0 and enemy4_position[0] < width:
        enemy4_position[0] += enemy4_speed
    else:
        enemy4_position[1] = random.randint(0, height-enemy4_size[0])
        enemy4_position[0] = 0

pygame.mixer.music.play(-1)

while not gameOver:
    player_direction = "player_"+str(direction)+".png"
    player_image = pygame.image.load(os.path.join("images", player_direction))
    player_image = pygame.transform.scale(player_image, (100+player_size_update, 85+player_size_update))
    player_size = [110+player_size_update, 110+player_size_update]

    for event in pygame.event.get():
        x = player_position[0]
        y = player_position[1]

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_position[0] >= 20:
                    x -= 50
                player_image = pygame.image.load(os.path.join("images", "player_left.png"))
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                if player_position[0] <= width-140:
                    x += 50
                player_image = pygame.image.load(os.path.join("images", "player_right.png"))
                direction = "right"
            elif event.key == pygame.K_UP:
                if player_position[1] >= 20:
                    y -= 50
            elif event.key == pygame.K_DOWN:
                if player_position[1] <= height-100:
                    y += 50

            player_image = pygame.transform.scale(player_image, (100+player_size_update, 85+player_size_update))

        player_position = [x, y]

    if enemy1_image:
        enemy_move()
    else: enemy_position = [-enemy1_size[0]-enemy1_size[0], -enemy1_size[1]-enemy1_size[1]]

    if enemy1_crash(player_position, enemy1_position):
        player_eat_direction = "player_eat_"+str(direction)+".png"
        player_image = pygame.image.load(os.path.join("images", player_eat_direction))
        player_image = pygame.transform.scale(player_image, (100+player_size_update, 85+player_size_update))
        enemy1_position = [width+enemy1_position[0], 0]
        pygame.mixer.Sound.play(eat_sound)
        player_size_update += 3

    if enemy2_crash(player_position, enemy2_position):
        player_eat_direction = "player_eat_"+str(direction)+".png"
        player_image = pygame.image.load(os.path.join("images", player_eat_direction))
        player_image = pygame.transform.scale(player_image, (100+player_size_update, 85+player_size_update))
        enemy2_position = [width+enemy2_position[0], 0]
        pygame.mixer.Sound.play(eat_sound)
        player_size_update += 0
        if player_size[0] < enemy2_size[0]+50:
            gameOver = True
            status = "lost"
        else:
            status  = "win"
            gameOver = True

    if enemy3_crash(player_position, enemy3_position):
        player_eat_direction = "player_eat_"+str(direction)+".png"
        player_image = pygame.image.load(os.path.join("images", player_eat_direction))
        player_image = pygame.transform.scale(player_image, (100+player_size_update, 85+player_size_update))
        enemy3_position = [width+enemy3_position[0], 0]
        pygame.mixer.Sound.play(eat_sound)
        player_size_update += 7
        if player_size[0] < enemy3_size[0]:
            gameOver = True
            player_size_update -= 5

    if enemy4_crash(player_position, enemy4_position):
        player_eat_direction = "player_eat_"+str(direction)+".png"
        player_image = pygame.image.load(os.path.join("images", player_eat_direction))
        player_image = pygame.transform.scale(player_image, (100+player_size_update, 85+player_size_update))
        enemy4_position = [width+enemy4_position[0], 0]
        pygame.mixer.Sound.play(eat_sound)
        player_size_update += 10
        if player_size[0] < enemy4_size[0]:
            gameOver = True
            player_size_update -= 7

    screen.blit(background, (0, 0))

    text = "Score: " + str(player_size_update)
    label = score_font.render(text, 1, (255, 255, 255))
    screen.blit(label, (20, 20))

    background_bubble_name = "bubble_background-"+str(count_bubble)+".png"
    background_bubble = pygame.image.load(os.path.join("bubble", background_bubble_name))
    background_bubble = pygame.transform.scale(background_bubble, (width, height-100))

    if count_bubble < 14:
        count_bubble += 1
        screen.blit(background_bubble, (0, 0))
    else: count_bubble = 0

    screen.blit(enemy1_image, (enemy1_position[0], enemy1_position[1]))
    screen.blit(enemy2_image, (enemy2_position[0], enemy2_position[1]))
    screen.blit(enemy3_image, (enemy3_position[0], enemy3_position[1]))
    screen.blit(enemy4_image, (enemy4_position[0], enemy4_position[1]))

    screen.blit(player_image, (player_position[0], player_position[1]))

    clock.tick(18)
    pygame.display.update()



endText = "Game Over"
endScore = "Your score: " + str(player_size_update)

print(status)
if status == "win":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background_wingame, (0, 0))
        pygame.display.update()
else:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        label_endgame = end_font.render(endText, 1, (255, 255, 255))
        label_endscore = end_font.render(endScore, 1, (255, 255, 255))

        text_endtext = label_endgame.get_rect(center=(width/2, height/2-150))
        text_endscore = label_endscore.get_rect(center=(width/2, height/2-60))

        screen.blit(background_endgame, (0, 0))

        screen.blit(label_endgame, text_endtext)
        screen.blit(label_endscore, text_endscore)

        clock.tick(18)
        pygame.display.update()