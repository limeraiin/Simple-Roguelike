import random
import pygame

# Minimum and maximum size of the room
MIN_ROOM_SIZE = 15
MAX_ROOM_SIZE = 20

# Probability that an enemy will be spawned in a room cell
ENEMY_SPAWN_PROBABILITY = 0.025

room_size = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
room = []
enemies = []  # List to store the coordinates of the enemy characters
for i in range(room_size):
    row = []
    for j in range(room_size):
        if i == 0 or i == room_size - 1 or j == 0 or j == room_size - 1:
            row.append('#')
        else:
            if random.random() < ENEMY_SPAWN_PROBABILITY:
                row.append('E')
                enemies.append((i, j))  # Add the coordinates of the enemy to the list
            else:
                row.append('.')
    room.append(row)

# Spawn the player at a random position in the room
player_i = random.randint(1, room_size - 2)
player_j = random.randint(1, room_size - 2)
room[player_i][player_j] = '@'

pygame.init()

screen = pygame.display.set_mode((room_size * 50, room_size * 50))

font = pygame.font.Font(None, 36)

for i, j in enemies:
    direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    # Calculate the position of the enemy
    new_i = i + direction[0]
    new_j = j + direction[1]
    # Check if the new position is valid
    if room[new_i][new_j] != '#' and room[new_i][new_j] != '@':
        room[i][j] = '.'  
        room[new_i][new_j] = 'E'  
        enemies.remove((i, j))  
        enemies.append((new_i, new_j))  

while True:
    for event in pygame.event.get():
        # Quit the game if the player closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Get the player's input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if room[player_i][player_j-1] != '#':
                room[player_i][player_j] = '.'
                player_j -= 1
                room[player_i][player_j] = '@'
        elif keys[pygame.K_a]:
            if room[player_i-1][player_j] != '#':
                room[player_i][player_j] = '.'
                player_i -= 1
                room[player_i][player_j] = '@'
        elif keys[pygame.K_s]:
            if room[player_i][player_j+1] != '#':
                room[player_i][player_j] = '.'
                player_j += 1
                room[player_i][player_j] = '@'
        elif keys[pygame.K_d]:
            if room[player_i+1][player_j] != '#':
                room[player_i][player_j] = '.'
                player_i += 1
                room[player_i][player_j] = '@'


    screen.fill((0, 0, 0))
    # Draw the room
    for i in range(room_size):
        for j in range(room_size):
            char = room[i][j]
            color = (255, 255, 255)  # Default color is white
            if char == 'E':
                color = (255, 0, 0)  # Set the color of the enemy to red
            text = font.render(char, True, color)
            screen.blit(text, (i * 50, j * 50))

    pygame.display.flip()
