from Board import Board
from setting import W, H
import pygame as pg

pg.init()
W, H = 600, 600
screen = pg.display.set_mode((W, H))

board = Board(W, H, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill('white')
    board.render(screen)
    pg.display.update()

