import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Tic-Tac-Toe")

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

board_cords = [(40, 20), (265, 20), (490, 20), (40, 250), (265, 250), (490, 250), (40, 480), (265, 480), (490, 480)]
enemy_cords = [(30, 20), (255, 20), (480, 20), (30, 250), (255, 250), (480, 250), (30, 480), (255, 480), (480, 480)]

def check_board():
    count = 0
    if 1 == board[0] or board[0] == 2:
        count += 1
    if 1 == board[1] or board[1] == 2:
        count += 1
    if 1 == board[2] or board[2] == 2:
        count += 1
    if 1 == board[3] or board[3] == 2:
        count += 1
    if 1 == board[4] or board[4] == 2:
        count += 1
    if 1 == board[5] or board[5] == 2:
        count += 1
    if 1 == board[6] or board[6] == 2:
        count += 1
    if 1 == board[7] or board[7] == 2:
        count += 1
    if 1 == board[8] or board[8] == 2:
        count += 1
    return count

def show_winner():
    winner = False
    bot = False
    if board[0] == 1 and board[1] == 1 and board[2] == 1:
        winner = True
    if board[3] == 1 and board[4] == 1 and board[5] == 1:
        winner = True
    if board[6] == 1 and board[7] == 1 and board[8] == 1:
        winner = True
    if board[0] == 1 and board[3] == 1 and board[6] == 1:
        winner = True
    if board[1] == 1 and board[4] == 1 and board[7] == 1:
        winner = True
    if board[2] == 1 and board[5] == 1 and board[8] == 1:
        winner = True
    if board[0] == 1 and board[4] == 1 and board[8] == 1:
        winner = True
    if board[2] == 1 and board[4] == 1 and board[6] == 1:
        winner = True
    if board[0] == 2 and board[1] == 2 and board[2] == 2:
        bot = True
    if board[3] == 2 and board[4] == 2 and board[5] == 2:
        bot = True
    if board[6] == 2 and board[7] == 2 and board[8] == 2:
        bot = True
    if board[0] == 2 and board[3] == 2 and board[6] == 2:
        bot = True
    if board[1] == 2 and board[4] == 2 and board[7] == 2:
        bot = True
    if board[2] == 2 and board[5] == 2 and board[8] == 2:
        bot = True
    if board[0] == 2 and board[4] == 2 and board[8] == 2:
        bot = True
    if board[2] == 2 and board[4] == 2 and board[6] == 2:
        bot = True
    return bot, winner

running = True
won = False
while running:
    pygame.draw.rect(screen, (255, 0, 0), (200, 0, 25, 650))
    pygame.draw.rect(screen, (255, 0, 0), (425, 0, 25, 650))
    pygame.draw.rect(screen, (255, 0, 0), (0, 200, 650, 25))
    pygame.draw.rect(screen, (255, 0, 0), (0, 425, 650, 25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] < 215 and pos[1] < 215 and board[0] != 1 and board[0] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[0])
                board.pop(0)
                board.insert(0, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif pos[0] < 215 and 215 < pos[1] < 415 and board[3] != 1 and board[3] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[3])
                board.pop(3)
                board.insert(3, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif pos[0] < 215 and 415 < pos[1] < 600 and board[6] != 1 and board[6] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[6])
                board.pop(6)
                board.insert(6, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif 215 < pos[0] < 415 and pos[1] < 215 and board[1] != 1 and board[1] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[1])
                board.pop(1)
                board.insert(1, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif 215 < pos[0] < 415 and 215 < pos[1] < 415 and board[4] != 1 and board[4] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[4])
                board.pop(4)
                board.insert(4, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif 215 < pos[0] < 415 and 415 < pos[1] < 600 and board[7] != 1 and board[7] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[7])
                board.pop(7)
                board.insert(7, 1)
                number = random.randint(0, 8)
                print(board)
                print(number)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif 415 < pos[0] < 600 and pos[1] < 215 and board[2] != 1 and board[2] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[2])
                board.pop(2)
                board.insert(2, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif 415 < pos[0] < 600 and 215 < pos[1] < 415 and board[5] != 1 and board[5] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[5])
                board.pop(5)
                board.insert(5, 1)
                number = random.randint(0, 8)
                print(number)
                print(board)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
            elif 415 < pos[0] < 600 and 415 < pos[1] < 600 and board[8] != 1 and board[8] != 2:
                font = pygame.font.Font(pygame.font.get_default_font(), 175)
                text_surface = font.render('X', True, (255, 0, 0))
                screen.blit(text_surface, board_cords[8])
                board.pop(8)
                board.insert(8, 1)
                number = random.randint(0, 8)
                print(number)
                print(check_board())
                if check_board() < 9:
                    while board[number] == 1 or board[number] == 2:
                        number = random.randint(0, 8)
                    board.pop(number)
                    board.insert(number, 2)
                    font = pygame.font.Font(pygame.font.get_default_font(), 175)
                    text_surface = font.render('O', True, (255, 0, 0))
                    screen.blit(text_surface, enemy_cords[number])
        bot, winner = show_winner()
        if not bot and not winner:
            if check_board() == 9:
                board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                screen.fill((0, 0, 0))
        elif not bot:
            board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            screen.fill((0, 0, 0))
        elif not winner:
            board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            screen.fill((0, 0, 0))
    pygame.display.update()
