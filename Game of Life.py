import pygame

WIDTH,HEIGHT = 1000,1000
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 60
WHITE = (200,200,200)
BLACK = (0,0,0)
rows,cols = 50,50
squares = [[False for i in range(rows)] for j in range(cols)]
squareHeight = HEIGHT/rows
squareWidth = WIDTH/cols
timestepsRun = False

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                checkKeyDown(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                checkMouseClick()
        draw_all()
    pygame.quit()

def draw_all():
    draw_window()
    draw_board()
    update_display()


def draw_board():
    for x in range(cols):
        for y in range(rows):
            xLoc = x * squareWidth
            yLoc = y * squareHeight
            if squares[x][y]:
                pygame.draw.rect(WINDOW, BLACK, [xLoc,yLoc, squareWidth,squareHeight])
                pygame.draw.rect(WINDOW, WHITE, [xLoc,yLoc, squareWidth,squareHeight],1)
            else: 
                pygame.draw.rect(WINDOW, BLACK, [xLoc,yLoc, squareWidth,squareHeight],1)
            
def checkMouseClick():
    mouse = pygame.mouse.get_pos()
    for x in range(cols):
        for y in range(rows):
            xLoc = squareWidth * x
            yLoc = squareHeight * y
            if xLoc <= mouse[0] <= (xLoc + squareWidth) and yLoc <= mouse[1] <= (yLoc + squareHeight):
                if squares[x][y]: 
                    squares[x][y] = False
                else: 
                    squares[x][y] = True

def checkNeighbours(x,y):
    neighbourCount = 0
    if (x-1) > -1 and (y-1) > -1 and squares[x-1][y-1]:
        neighbourCount += 1
    if (y-1) > -1 and squares[x][y-1]:
        neighbourCount += 1
    if (x+1) < (cols-1) and (y-1) > -1 and squares[x+1][y-1]:
        neighbourCount += 1
    if (x-1) > -1 and squares[x-1][y]:
        neighbourCount += 1
    if (x+1) < (cols-1) and squares[x+1][y]:
        neighbourCount += 1
    if (x-1) > -1 and (y+1) < (rows-1) and squares[x-1][y+1]:
        neighbourCount += 1
    if (y+1) < (rows-1) and squares[x][y+1]:
        neighbourCount += 1 
    if (x+1) < (cols-1) and (y+1) < (rows-1) and squares[x+1][y+1]:
        neighbourCount += 1
    return neighbourCount

def checkKeyDown(event):
    global timestepsRun
    if event.key == pygame.K_r:
        resetBoard()
    if event.key == pygame.K_SPACE:
        timeStep()
    if event.key == pygame.K_t:
        if timestepsRun:
            timestepsRun = False
        else:
            timestepsRun = True

def timeStep():
    global squares
    states = [[False for i in range(rows)] for j in range(cols)]
    for x in range(cols):
        for y in range(rows):
            neighbours = checkNeighbours(x,y)
            if squares[x][y]:
                if neighbours < 2:
                    states[x][y] = False
                if neighbours == 2 or neighbours == 3:
                    states[x][y] = True
                if neighbours > 3:
                    states[x][y] = False
            else:
                if neighbours == 3:
                    states[x][y] = True
    for x in range(cols):
        for y in range(rows):
            squares[x][y] = states[x][y]


def resetBoard():
    for x in range(cols):
        for y in range(rows):
            squares[x][y] = False

def draw_window():
    WINDOW.fill(WHITE)

def update_display():
    pygame.display.update()

if __name__ == "__main__":
    main()

