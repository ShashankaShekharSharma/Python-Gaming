import pygame
import random

# Initialize pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 40
MAZE_WIDTH, MAZE_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the maze
maze = []
for i in range(MAZE_HEIGHT):
    row = []
    for j in range(MAZE_WIDTH):
        if random.random() < 0.2:
            row.append(1)
        else:
            row.append(0)
    maze.append(row)

# Set up the player
player_pos = [1, 1]
player_size = TILE_SIZE

# Set up the endpoint
endpoint_pos = [MAZE_WIDTH - 2, MAZE_HEIGHT - 2]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up the clock
clock = pygame.time.Clock()

def draw_maze():
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x, y = j * TILE_SIZE, i * TILE_SIZE
            if cell == 1:
                pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))

def draw_player():
    pygame.draw.rect(screen, RED, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, player_size, player_size))

def draw_endpoint():
    pygame.draw.rect(screen, GREEN, (endpoint_pos[0] * TILE_SIZE, endpoint_pos[1] * TILE_SIZE, player_size, player_size))

def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0 and maze[player_pos[1]][player_pos[0] - 1] == 0:
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and player_pos[0] < MAZE_WIDTH - 1 and maze[player_pos[1]][player_pos[0] + 1] == 0:
        player_pos[0] += 1
    if keys[pygame.K_UP] and player_pos[1] > 0 and maze[player_pos[1] - 1][player_pos[0]] == 0:
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and player_pos[1] < MAZE_HEIGHT - 1 and maze[player_pos[1] + 1][player_pos[0]] == 0:
        player_pos[1] += 1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    handle_input()

    # Check if the player reached the endpoint
    if player_pos == endpoint_pos:
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_maze()
    draw_player()
    draw_endpoint()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
