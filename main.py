# MEMORY PUZZLE
# BY yarik21yt
# IT WILL BE UPLOADED ON MY GITHUB PAGE

import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()

FPS = 30
WIDTH = 600
HEIGHT = 600
SPEED_BOX = 10
SIZE_BOX = 40
GAP_BOX = 10
COUNT_BOX_WIDTH = 10
COUNT_BOX_HEIGHT = 10


#colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (240, 240, 240)
LIGHT_BLUE = (0, 100, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (153, 0, 0)
PINK = (255, 100, 100)
LIME = (0, 255, 0)
MELON = (249, 248, 187)  #NOT WATERMELON!!!!
DARK_GREEN_TEA = (186, 219, 173)
PEACH = (255, 229, 180)
BUBBLE_GUM = (255, 193, 204)
YELLOW = (255, 255, 0)
FOXIA = (255, 0, 127)
ORANGE = (255, 128, 0)
BIRUS = (0, 153, 153)
FIOLET = (76, 0, 153)
DARK_ORANGE = (153, 76, 0)




BG_COLOR = PINK
BOX_COLOR = WHITE
TITLE_TEXT_COLOR = PEACH

#game shapes
CIRCLE = "circle"
SQUARE = "square"
TRIANGLE = "triangle"
ROMB = "romb"
OVAL = "oval"

ALL_SHAPES = (CIRCLE, SQUARE, TRIANGLE, ROMB, OVAL)
ALL_COLORS = (FOXIA, YELLOW, BLUE, BLACK, RED, LIME, MELON, BIRUS, DARK_ORANGE, FIOLET)




FPS_CLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MEMORY_PUZZLE")

mouse_x = 0
mouse_y = 0

font = pygame.font.Font("makinggames/MarioFontv3Remakefull.ttf", 30)
font_surface = font.render("MEMORY PUZZLE", True, TITLE_TEXT_COLOR)
font_rect = font_surface.get_rect()
font_rect.midtop = (WIDTH / 2, 25)


def draw_shape(shape, color, box_x, box_y):
    left = box_x * (SIZE_BOX + GAP_BOX) + 50
    top = box_y * (SIZE_BOX + GAP_BOX) + 80
    half = int(SIZE_BOX / 2)
    quarter = int(half / 2)
    if shape == CIRCLE:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), quarter)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, half, half))
    elif shape == TRIANGLE:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top + quarter), (left + half + quarter, top + half + quarter), (left + quarter, top + half + quarter)))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left + 5, top + quarter, half + quarter, half))
    elif shape == ROMB:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top + quarter), (left + half + quarter, top + half), (left + half, top + half + quarter), (left + quarter, top + half)))




def draw_board(board, data_board):
    DISPLAYSURF.blit(font_surface, font_rect)
    for box_y in range(COUNT_BOX_HEIGHT):
        for box_x in range(COUNT_BOX_WIDTH):
            left = box_x * (SIZE_BOX + GAP_BOX) + 50
            top = box_y * (SIZE_BOX + GAP_BOX) + 80
            if data_board[box_y][box_x]:
                shape, color = board[box_y][box_x]
                draw_shape(shape, color, box_x, box_y)
            else:
                pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, SIZE_BOX, SIZE_BOX))





def random_board():
    icons = []
    for shape in ALL_SHAPES:
        for color in ALL_COLORS:
            icons.append((shape, color))
    icons = icons * 2
    random.shuffle(icons)
    board = []
    for y in range(COUNT_BOX_HEIGHT):
        row = []
        for x in range(COUNT_BOX_WIDTH):
            row.append(icons[0])
            icons.pop(0)
        board.append(row)
    return board

def generate_data_board():
    board = []
    for y in range(COUNT_BOX_HEIGHT):
        row = []
        for x in range(COUNT_BOX_WIDTH):
            row.append(False)
        board.append(row)
    return board





def get_box(x, y):
    for box_y in range(COUNT_BOX_HEIGHT):
        for box_x in range(COUNT_BOX_WIDTH):
            left = box_x * (SIZE_BOX + GAP_BOX) + 50
            top = box_y * (SIZE_BOX + GAP_BOX) + 80
            box = pygame.Rect(left, top, SIZE_BOX, SIZE_BOX)
            if box.collidepoint(x, y):
                return (box_x, box_y)
    return (None, None)




def check_win(board):
    for box_y in range(COUNT_BOX_HEIGHT):
        for box_x in range(COUNT_BOX_WIDTH):
            if board[box_y][box_x] == False:
                return False
    return True






board = random_board()
data_board = generate_data_board()
print(data_board)
opened_blocks = []
opened_blocks_pos = []
current_time = None
delay = 0.2
win = 0
font = pygame.font.Font("makinggames/MarioFontv3Remakefull.ttf", 46)
win_surface = font.render("YOU WON!!!!!!!!", True, (250, 102, 156))
win_rect = win_surface.get_rect()
win_rect.midtop = (WIDTH / 2, 25)
font_h2 = pygame.font.Font("makinggames/MarioFontv3Remakefull.ttf", 30)
result_surface = font_h2.render("Your results:", True, (250, 135, 52))
result_rect = result_surface.get_rect()
result_rect.midtop = (WIDTH / 2, HEIGHT / 2 - 100)
start_time = time.time()
win_time = 0
clicks = 0

while True:
    mouse_click = False



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mouse_click = True
            mouse_x, mouse_y = event.pos
            clicks += 1
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
    if win == 0:
        DISPLAYSURF.fill(BG_COLOR)
        draw_board(board, data_board)
        if mouse_click:
            box_x, box_y = get_box(mouse_x, mouse_y)
            if box_x is not None and box_y is not None and (box_x, box_y) not in opened_blocks_pos:
                data_board[box_y][box_x] = True
                opened_blocks.append(board[box_y][box_x])
                opened_blocks_pos.append((box_x, box_y))
                print(data_board)
                print(opened_blocks)
                print(opened_blocks_pos)
                if len(opened_blocks) == 2:
                    if opened_blocks[0] == opened_blocks[1] and opened_blocks_pos[0] != opened_blocks_pos[1]:
                        opened_blocks = []
                        opened_blocks_pos = []
                    else:
                        current_time = time.time()

        if current_time is not None and time.time() - current_time > delay:
            for box_x, box_y in opened_blocks_pos:
                data_board[box_y][box_x] = False
            opened_blocks = []
            opened_blocks_pos = []
            current_time = None

        if check_win(data_board):
            win = 1
            win_time = time.time() - start_time
        else:
            win = 0
    if win == 1:
        DISPLAYSURF.fill((204, 255, 255))
        DISPLAYSURF.blit(win_surface, win_rect)
        DISPLAYSURF.blit(result_surface, result_rect)
        clicks_surface = font_h2.render(f"All clicks: {clicks}", True, (250, 135, 52))
        clicks_surface_2 = font_h2.render(f"Time used: {round(win_time / 60, 2)} minutes", True, (250, 135, 52))
        clicks_rect_2 = clicks_surface_2.get_rect()
        clicks_rect_2.midtop = (WIDTH / 2, HEIGHT / 2 - 20)
        clicks_rect = clicks_surface.get_rect()
        clicks_rect.midtop = (WIDTH / 2, HEIGHT / 2 - 60)
        DISPLAYSURF.blit(clicks_surface, clicks_rect)
        DISPLAYSURF.blit(clicks_surface_2, clicks_rect_2)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
