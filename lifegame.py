import pygame
import sys
import cfg
import time


WHITE = cfg.WHITE
WINDOW_HEIGHT = cfg.WINDOW_HEIGHT
WINDOW_WIDTH = cfg.WINDOW_HEIGHT
blockSize = cfg.blockSize
color = []
neighbours = []
for i in range(0,1010):
    color.append([])
    for j in range(0,1010):
        color[i].append(WHITE)
for i in range(0,1010):
    neighbours.append([])
    for j in range(0,1010):
        neighbours[i].append(0)

def update():
    for x in range(0, WINDOW_WIDTH, blockSize):
        x //= blockSize
        for y in range(0, WINDOW_HEIGHT, blockSize):
            y //= blockSize
            neighbours[x][y] = 0
    for x in range(0, WINDOW_WIDTH, blockSize):
        x //= blockSize
        for y in range(0, WINDOW_HEIGHT, blockSize):
            y //= blockSize
            if color[x-1][y-1] == cfg.BLACK and x-1 >= 0 and y-1 >= 0:
                neighbours[x][y] += 1
            if color[x][y-1] == cfg.BLACK and y-1 >= 0:
                neighbours[x][y] += 1
            if color[x+1][y-1] == cfg.BLACK and x+1 <= len(color) - 1 and y-1 >= 0:
                neighbours[x][y] += 1
            if color[x-1][y] == cfg.BLACK and x-1 >= 0:
                neighbours[x][y] += 1
            if color[x+1][y] == cfg.BLACK and x+1 <= len(color) - 1:
                neighbours[x][y] += 1
            if color[x-1][y+1] == cfg.BLACK and x-1 >= 0 and y+1 <= len(color) - 1:
                neighbours[x][y] += 1
            if color[x][y+1] == cfg.BLACK and y+1 <= len(color) - 1:
                neighbours[x][y] += 1
            if color[x+1][y+1] == cfg.BLACK and x+1 <= len(color) - 1 and y+1 <= len(color) - 1:
                neighbours[x][y] += 1
    for x in range(0, WINDOW_WIDTH, blockSize):
        x //= blockSize
        for y in range(0, WINDOW_HEIGHT, blockSize):
            y //= blockSize
            if color[x][y] == WHITE and neighbours[x][y] == 3:
                color[x][y]  = cfg.BLACK
            elif color[x][y] == cfg.BLACK and neighbours[x][y] != 2 and neighbours[x][y] != 3:
                color[x][y] = WHITE
                


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    enterClicked = False
    while enterClicked == False:
        drawGrid()
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_x:
                    x = pygame.mouse.get_pos()[0]//blockSize
                    y = pygame.mouse.get_pos()[1]//blockSize
                    color[x][y] = WHITE if color[x][y] == cfg.BLACK else cfg.BLACK
                if e.key == pygame.K_RETURN:
                    enterClicked = True
    while True:
        update()
        drawGrid()
        time.sleep(0.2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        print(e.key)
        pygame.display.update()


def drawGrid():
 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, color[x//blockSize][y//blockSize], rect, blockSize//2)

if __name__ == "__main__":
    main()