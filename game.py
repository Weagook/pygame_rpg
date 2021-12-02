import pygame, sys, time, random


with open('map.csv', 'r') as file:
    map = file.readlines()
maps = []
for item in map:
    row = []
    rows = item.replace('\n', '').split(',')
    for item1 in rows:
        row.append(item1)
    maps.append(row)


pygame.init()

size = width, height = 640, 700

white = 255, 255, 255
orange_red = 255, 69, 0

tile_size = 32
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

screen.fill(white)

wall = pygame.image.load('sprites/cobblestone.png')
chest = pygame.image.load('sprites/chest.png')
hero = pygame.image.load('sprites/knight.png')
goblin = pygame.image.load('sprites/enemy.png')
back = pygame.image.load('sprites/floor.png')
empty = pygame.image.load('sprites/empty.png')
empty = pygame.transform.scale(empty, (640,300))
emptyrect = empty.get_rect()
# print(dir(emptyrect))
backrect = back.get_rect()
wallrect = wall.get_rect()
chestrect = chest.get_rect()
herorect = hero.get_rect()
goblinrect = goblin.get_rect()

class Font(object):
    def __init__(self):
        self.text = pygame.font.SysFont('Times New Roman', 30)
        self.color = orange_red
        self.damage = self.text.render('Damage: 30', True, self.color)
        self.hp_panel = self.text.render(f'HP: {man.hp}', True, self.color)
        emptyrect.left = 0
        emptyrect.top = 640
        screen.blit(empty, emptyrect)
        screen.blit(self.hp_panel, (0, 670))
        screen.blit(self.damage, (0, 640))

    # def enemy_panel(self):


class Hero(object):
    def __init__(self, hero, x, y):
        self.hero = hero
        self.herorect = hero.get_rect()
        self.x = x
        self.y = y
        self.hp = 100

    def draw_empty(self):
        back= pygame.image.load("sprites/floor.png")
        backrect = back.get_rect()
        backrect.left= self.x * 32
        backrect.top= self.y * 32
        screen.blit(back,backrect)

    def draw(self):
        self.herorect.top=self.y * 32
        self.herorect.left=self.x * 32
        screen.blit(self.hero, self.herorect)

    def move_right(self):
        if maps[self.y][self.x + 1] == '3':
            self.hp -= random.randint(1, 10)
            font = Font()
            if self.hp <= 0:
                print('GAME OVER!')
                time.sleep(3)
                sys.exit()
        elif maps[self.y][self.x + 1] != '0':
            man.draw_empty()
            self.x += 1
            man.draw()

    def move_left(self):
        if maps[self.y][self.x - 1] == '3':
            pass
        elif maps[self.y][self.x - 1] != '0':
            man.draw_empty()
            self.x -= 1
            man.draw()

    def move_down(self):
        if maps[self.y+1][self.x] == '3':
            pass
        elif maps[self.y+1][self.x] != '0':
            man.draw_empty()
            self.y += 1
            man.draw()

    def move_up(self):
        if maps[self.y-1][self.x] == '3':
            pass

        if maps[self.y-1][self.x] != '0':
            man.draw_empty()
            self.y -= 1
            man.draw()

class Enemy(object):
    def __init__(self, enemy, x, y):
        self.enemy = enemy
        self.enemyrect = enemy.get_rect()
        self.x = x
        self.y = y
        self.hp = 100

    def draw(self):
        self.enemyrect.top=self.y * 32
        self.enemyrect.left=self.x * 32
        screen.blit(self.enemy, self.enemyrect)


enemy_list = []
x = 0
y = -1
for col in maps:
    y += 1
    x = -1
    for row in col:
        x += 1
        if row == '0':
            wallrect.top = y * 32
            wallrect.left = x * 32
            screen.blit(wall, wallrect)
        if row == '1':
            backrect.top = y * 32
            backrect.left = x * 32
            screen.blit(back, backrect)
        if row == '2':
            backrect.top = y * 32
            backrect.left = x * 32
            screen.blit(back, backrect)
            man = Hero(hero, x, y)
            man.draw()
        if row == '3':
            backrect.top = y * 32
            backrect.left = x * 32
            screen.blit(back, backrect)
            enemy = Enemy(goblin, x, y)
            enemy.draw()
            enemy_list.append(enemy)
        if row == '4':
            backrect.top = y * 32
            backrect.left = x * 32
            screen.blit(back, backrect)
            chestrect.top = y * 32
            chestrect.left = x * 32
            screen.blit(chest, chestrect)
font = Font()
# pygame.display.update()
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                man.move_up()
                pygame.display.flip()
            if event.key == pygame.K_LEFT:
                man.move_left()
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                man.move_right()
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                man.move_down()
                pygame.display.flip()
    clock.tick(60)
