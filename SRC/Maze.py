import pygame
import random

class MazeGame:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 640, 480
        self.TILE_SIZE = 40
        self.MAZE_WIDTH, self.MAZE_HEIGHT = self.WIDTH // self.TILE_SIZE, self.HEIGHT // self.TILE_SIZE

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.maze = []
        for i in range(self.MAZE_HEIGHT):
            row = []
            for j in range(self.MAZE_WIDTH):
                if random.random() < 0.2:
                    row.append(1)
                else:
                    row.append(0)
            self.maze.append(row)

        self.player_pos = [1, 1]
        self.player_size = self.TILE_SIZE

        self.endpoint_pos = [self.MAZE_WIDTH - 2, self.MAZE_HEIGHT - 2]

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Maze Game")

        self.clock = pygame.time.Clock()

    def draw_maze(self):
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x, y = j * self.TILE_SIZE, i * self.TILE_SIZE
                if cell == 1:
                    pygame.draw.rect(self.screen, self.WHITE, (x, y, self.TILE_SIZE, self.TILE_SIZE))

    def draw_player(self):
        pygame.draw.rect(self.screen, self.RED,
                         (self.player_pos[0] * self.TILE_SIZE, self.player_pos[1] * self.TILE_SIZE,
                          self.player_size, self.player_size))

    def draw_endpoint(self):
        pygame.draw.rect(self.screen, self.GREEN,
                         (self.endpoint_pos[0] * self.TILE_SIZE, self.endpoint_pos[1] * self.TILE_SIZE,
                          self.player_size, self.player_size))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_pos[0] > 0 and self.maze[self.player_pos[1]][self.player_pos[0] - 1] == 0:
            self.player_pos[0] -= 1
        if keys[pygame.K_RIGHT] and self.player_pos[0] < self.MAZE_WIDTH - 1 \
                and self.maze[self.player_pos[1]][self.player_pos[0] + 1] == 0:
            self.player_pos[0] += 1
        if keys[pygame.K_UP] and self.player_pos[1] > 0 and self.maze[self.player_pos[1] - 1][self.player_pos[0]] == 0:
            self.player_pos[1] -= 1
        if keys[pygame.K_DOWN] and self.player_pos[1] < self.MAZE_HEIGHT - 1 \
                and self.maze[self.player_pos[1] + 1][self.player_pos[0]] == 0:
            self.player_pos[1] += 1

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_input()

            if self.player_pos == self.endpoint_pos:
                running = False

            self.screen.fill(self.BLACK)
            self.draw_maze()
            self.draw_player()
            self.draw_endpoint()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = MazeGame()
    game.run_game()
