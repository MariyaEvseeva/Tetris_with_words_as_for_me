import pygame
import random

pygame.font.init()

# Глобальные переменные
s_width = 750
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# спрайты
all_sprites = pygame.sprite.Group()

# формы падающих фигур
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, L, T]

# цвета фигур
shape_colors = [(250, 128, 114),         # красный оттенок
                (255, 160, 122),         # оранжевый оттенок
                (253, 246, 177),         # желтый оттенок
                (144, 238, 144),         # зеленый оттенок
                (0, 206, 209),           # голубой оттенок
                (147, 112, 219)]         # фиолетовый оттенок


# загрузка изображения
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image

# Неудавшаяся работа со спрайтами, частично.
'''
def generate_figure(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '0':
                Tile('letter', x, y)
                new_player = Player(x, y)
    return x, y

def load_level(filename):
    filename = 'data/' + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


level_x, level_y = generate_level(load_level("level.txt"))'''

'''
all_sprites = pygame.sprite.Group()


class a(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

a = a(200, 'а.png')

class b(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

b = b(200, 'б.png')

class v(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

v = v(200, 'в.png')

class g(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

g = g(200, 'г.png')

class d(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

d = d(200, 'д.png')

class e(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

e = e(200, 'е.png')

class ee(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

ee = ee(200, 'ё.png')

class zh(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

zh = zh(200, 'ж.png')

class z(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

z = z(200, 'з.png')

class iiii(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

iiii = iiii(200, 'и.png')

class i_short(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

i_short = i_short(200, 'й.png')

class k(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

k = k(200, 'к.png')

class L(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

L = L(200, 'л.png')

class m(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

m = m(200, 'м.png')

class n(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

n = n(200, 'н.png')

class OO(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

OO = OO(200, 'о.png')

class p(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

p = p(200, 'п.png')

class r(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

r = r(200, 'р.png')

class s(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

s = s(200, 'с.png')

class t(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

t = t(200, 'т.png')

class u(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

u = u(200, 'у.png')

class f(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

f = f(200, 'ф.png')

class kh(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

kh = kh(200, 'х.png')

class ts(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

ts = ts(200, 'ц.png')

class ch(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

ch = ch(200, 'ч.png')

class sh(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

sh = sh(200, 'ш.png')

class shch(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

shch = shch(200, 'щ.png')

class strong_symbol(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

strong_symbol = strong_symbol(200, 'ъ.png')

class y(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

y = y(200, 'ы.png')

class soft_symbol(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

soft_symbol = soft_symbol(200, 'ь.png')

class strong_e(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

strong_e = strong_e(200, 'э.png')

class yu(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

yu = yu(200, 'ю.png')

class ya(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image1 = pygame.transform.scale(self.image, (30, 30))
        self.image1.set_colorkey((0, 0, 0))
        self.rect = self.image1.get_rect(center=(30, 30))

ya = ya(200, 'я.png')
'''


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


# делаем решетку
def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(10)] for y in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)]
                    for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


# "comicsans"
def draw_text(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                         top_left_y +
                         play_height / 2 - label.get_height() / 2))


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size),
                         (sx + play_width, sy + i * block_size))

        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128),
                             (sx + j * block_size, sy),
                             (sx + j * block_size,
                              sy + play_height))


def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 30)
    color4 = pygame.Color('#9370DB')
    label = font.render('Следущая:', 1, color4)

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * block_size,
                                                        sy + i * block_size,
                                                        block_size,
                                                        block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface, grid):
    fon_color = pygame.Color('#ADD8E6')
    screen.fill(fon_color)

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 65)
    color3 = pygame.Color('#5F9EA0')
    label = font.render('ТЕТРИС', 1, (color3))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                         30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size,
                                                   top_left_y + i * block_size,
                                                   block_size, block_size), 0)

    color_of_the_line = pygame.Color('#F5F5DC')
    pygame.draw.rect(surface, color_of_the_line, (top_left_x,
                                                  top_left_y,
                                                  play_width,
                                                  play_height), 5)

    draw_grid(surface, grid)


def main(screen):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    item = get_shape()
    next_item = get_shape()
    clock = pygame.time.Clock()
    falling = 0
    speed = 0.25
    time = 0

    running = True
    while running:
        grid = create_grid(locked_positions)
        falling += clock.get_rawtime()
        time += clock.get_rawtime()
        clock.tick()

        if time / 1000 > 5:
            time = 0
            if time > 0.12:
                time -= 0.005

        if falling / 1000 > speed:
            falling = 0
            item.y += 1
            if not(valid_space(item, grid)) and item.y > 0:
                item.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    item.x += 1
                    if not(valid_space(item, grid)):
                        item.x -= 1
                if event.key == pygame.K_LEFT:
                    item.x -= 1
                    if not(valid_space(item, grid)):
                        item.x += 1
                if event.key == pygame.K_UP:
                    item.rotation += 1
                    if not(valid_space(item, grid)):
                        item.rotation -= 1

        shape_pos = convert_shape_format(item)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = item.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = item.color
            item = next_item
            next_item = get_shape()
            change_piece = False

        draw_window(screen, grid)
        draw_next_shape(next_item, screen)
        pygame.display.update()

        if check_lost(locked_positions):
            color2 = pygame.Color('#008080')
            draw_text(screen, 'Конец игры', 80, color2)
            pygame.display.update()
            pygame.time.delay(1500)
            running = False


def start(screen):
    run = True
    while run:
        fon_color = pygame.Color('#6495ED')
        screen.fill(fon_color)
        color = pygame.Color('#4682B4')
        draw_text(screen, 'Нажмите пробел, чтобы начать', 45, color)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(screen)

    pygame.display.quit()


screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
start(screen)
