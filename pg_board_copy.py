import pygame

def cr_to_xy(key):
    return key[0]*field, key[1]*field

def xy_to_cr(key):
    return key[0]//field, key[1]//field

def draw_board(board):
    for key, value in board.items():
        color = '#DFBF93' if value else '#C5844E'
        pygame.draw.rect(screen, color, (*cr_to_xy(key), field, field))

def fen_to_location(fen):
    location, c, r = {}, 0, 0
    figurenstellung, zugrecht, rochaderechte, enpassant, zug50, zugnummer = fen.split()
    for char in figurenstellung:
        if char.isalpha():
            location[(c,r)] = char
            c += 1
        elif char.isnumeric():
            c += int(char)
        else:
            c,r = 0, r+1
    return location, zugrecht

def image_load():
    images = {}
    figure_to_img_loc = dict(r='br', n='bn', b='bb', q='bq', k='bk', p='bp',
                             R='wr', N='wn', B='wb', Q='wq', K='wk', P='wp')
    for char, img_path in figure_to_img_loc.items():
        img = pygame.image.load(f'images/{img_path}.png')
        images[char] = pygame.transform.smoothscale(img, (field, field))
    return images

def draw_figures(location):
    for cr, char in location.items():
        screen.blit(figures[char], cr_to_xy(cr))


pygame.init()
width, height = 800, 800
size = width, height
field = width // 8
fps = 40
screen = pygame.display.set_mode((size))
board = {(c,r): c %2 == r %2 for c in range(8) for r in range(8)}
fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

location, on_turn = fen_to_location(fen)
figures = image_load()

# font = pygame.font.Font('freesansbold.ttf', 20)
# text = font.render(on_turn, True, (255, 255, 255))
# textRect = text.get_rect()
# textRect.center = (field*9, field*2)

running = True
clock = pygame.time.Clock()
drag = None

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not drag:
            start = xy_to_cr(pygame.mouse.get_pos())
            if start in location:
                figur = location[start]
                drag = figures[figur]
                del location[start]
        elif event.type == pygame.MOUSEBUTTONUP and drag:
            stop = xy_to_cr(pygame.mouse.get_pos())
            location[stop] = figur
            drag = None

    screen.fill((0,0,0))
    draw_board(board)
    draw_figures(location)
    if drag:
        rect = drag.get_rect(center=pygame.mouse.get_pos())
        screen.blit(drag, rect)
    print(location)

    pygame.display.flip()
pygame.quit()