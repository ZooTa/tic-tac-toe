import pygame

pygame.init()

win = pygame.display.set_mode((700, 700))

pygame.display.set_caption('Tic-Tac-Toe')

first = pygame.draw.rect(win, (255,255,255), (25,25,200,200))
second = pygame.draw.rect(win, (255,255,255), (250,25,200,200))
third = pygame.draw.rect(win, (255,255,255), (475,25,200,200))
fourth = pygame.draw.rect(win, (255,255,255), (25,250,200,200))
fifth = pygame.draw.rect(win, (255,255,255), (250,250,200,200))
sixth = pygame.draw.rect(win, (255,255,255), (475,250,200,200))
seventh = pygame.draw.rect(win, (255,255,255), (25,475,200,200))
eighth = pygame.draw.rect(win, (255,255,255), (250,475,200,200))
ninth = pygame.draw.rect(win, (255,255,255), (475,475,200,200))

draw_object = 'circle'
times = 0
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

run = True

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
turn = "rect"


def printt():
    print("---------")
    for row in board:
        for column in row:
            print(column, end="   ")
        print()
    print("---------")


def is_winning():
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != " ":
        pygame.quit()
        if board[0][0] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != " ":
        pygame.quit()
        if board[1][0] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != " ":
        pygame.quit()
        if board[2][0] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != " ":
        pygame.quit()
        if board[0][0] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != " ":
        pygame.quit()
        if board[0][1] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != " ":
        pygame.quit()
        if board[0][2] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ":
        pygame.quit()
        if board[0][0] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif board[0][2] == board[1][1] and board[0][0] == board[2][0] and board[0][2] != " ":
        pygame.quit()
        if board[0][2] == "X":
            print("player 2 win")
        else:
            print("player 1 win")
    elif times == 9:
        pygame.quit()
        print("it's a tie")
    else:
        win = False


def insert(r, c):
    if draw_object == "rect":
        board[r][c] = "X"

    if draw_object == "circle":
        board[r][c] = "O"


while run:

    pygame.time.delay(100)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True
                run = True
                board = [[" ", " ", " "],
                         [" ", " ", " "],
                         [" ", " ", " "]]
                printt()

                first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 200, 200))
                second = pygame.draw.rect(win, (255, 255, 255), (250, 25, 200, 200))
                third = pygame.draw.rect(win, (255, 255, 255), (475, 25, 200, 200))
                fourth = pygame.draw.rect(win, (255, 255, 255), (25, 250, 200, 200))
                fifth = pygame.draw.rect(win, (255, 255, 255), (250, 250, 200, 200))
                sixth = pygame.draw.rect(win, (255, 255, 255), (475, 250, 200, 200))
                seventh = pygame.draw.rect(win, (255, 255, 255), (25, 475, 200, 200))
                eighth = pygame.draw.rect(win, (255, 255, 255), (250, 475, 200, 200))
                ninth = pygame.draw.rect(win, (255, 255, 255), (475, 475, 200, 200))

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if win != True:
                if first.collidepoint(pos) and first_open:
                    times = times + 1
                    insert(0, 0)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (125, 125), 75)
                        pygame.draw.circle(win, (255, 255, 255), (125, 125), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (50, 50, 150, 150))
                        draw_object = 'circle'
                    first_open = False
                    printt()

                if second.collidepoint(pos) and second_open:
                    times = times + 1
                    insert(0, 1)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (350, 125), 75)
                        pygame.draw.circle(win, (255, 255, 255), (350, 125), 65)
                        draw_object = 'rect'
                    else:

                        pygame.draw.rect(win, (255, 0, 0), (275, 50, 150, 150))
                        draw_object = 'circle'
                    second_open = False
                    printt()

                if third.collidepoint(pos) and third_open:
                    times = times + 1
                    insert(0, 2)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (575, 125), 75)
                        pygame.draw.circle(win, (255, 255, 255), (575, 125), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (500, 50, 150, 150))
                        draw_object = 'circle'
                    third_open = False
                    printt()

                if fourth.collidepoint(pos) and fourth_open:
                    times = times + 1
                    insert(1, 0)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (125, 350), 75)
                        pygame.draw.circle(win, (255, 255, 255), (125, 350), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (50, 275, 150, 150))
                        draw_object = 'circle'
                    fourth_open = False
                    printt()

                if fifth.collidepoint(pos) and fifth_open:
                    times = times + 1
                    insert(1, 1)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (350, 350), 75)
                        pygame.draw.circle(win, (255, 255, 255), (350, 350), 65)

                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (275, 275, 150, 150))
                        draw_object = 'circle'
                    fifth_open = False
                    printt()

                if sixth.collidepoint(pos) and sixth_open:
                    times = times + 1
                    insert(1, 2)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (575, 350), 75)
                        pygame.draw.circle(win, (255, 255, 255), (575, 350), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (500, 275, 150, 150))
                        draw_object = 'circle'
                    sixth_open = False
                    printt()

                if seventh.collidepoint(pos) and seventh_open:
                    times = times + 1
                    insert(2, 0)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (125, 575), 75)
                        pygame.draw.circle(win, (255, 255, 255), (125, 575), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (50, 500, 150, 150))
                        draw_object = 'circle'
                    seventh_open = False
                    printt()

                if eighth.collidepoint(pos) and eighth_open:
                    times = times + 1
                    insert(2, 1)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (350, 575), 75)
                        pygame.draw.circle(win, (255, 255, 255), (350, 575), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (275, 500, 150, 150))
                        draw_object = 'circle'
                    eighth_open = False
                    printt()

                if ninth.collidepoint(pos) and ninth_open:
                    times = times + 1
                    insert(2, 2)
                    if draw_object == 'circle':
                        pygame.draw.circle(win, (0, 0, 255), (575, 575), 75)
                        pygame.draw.circle(win, (255, 255, 255), (575, 575), 65)
                        draw_object = 'rect'
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (500, 500, 150, 150))
                        draw_object = 'circle'
                    ninth_open = False
                    printt()

    pygame.display.update()
    is_winning()
pygame.quit()