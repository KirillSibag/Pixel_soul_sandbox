import keyboard
import pygame


class player():#класс игрока
    def __init__(self, img_adress = 'imgs/player.png'):
        self.image = pygame.image.load(img_adress) #оригинальное изображение
        image_flip = self.image
        self.image_flip = pygame.transform.flip(image_flip, True, False)#отражённое изображение
        self.image_show = self.image
        self.image_x = 20   #положение по горизонтали
        self.image_y = 20   #положение по вертикали

    def move(self, horisontal, vertical):
        #изменение положения игрока
        self.image_x += horisontal
        self.image_y += vertical

types = {"mushroom": {"adress" : "imgs/objs/mushroom.png","nutrition": 3,"poison": 0,"tyagely": 0}, "bottle" : {"adress" : "imgs/objs/bottle.png","nutrition": 3,"poison": 0,"tyagely": 0}}
class object():#класс объектов, к которым применимы операции выпадения, получения и преобразования
    def __init__(self, type, x, y):
        self.nutrition = types[type]["nutrition"]
        self.poison = types[type]["poison"]
        self.tyagely = types[type]["tyagely"]
        self.x = x
        self.y = y

        self.image = pygame.image.load(types[type]["adress"])  # оригинальное изображение
        self.image_show = self.image


pygame.init()
screen = pygame.display.set_mode((1140, 540))
done = False

clock = pygame.time.Clock()

player = player()
objs = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #определение нажатых клавиш
    pressed = pygame.key.get_pressed()

    #определение направления движения
    horisontal = pressed[pygame.K_d] - pressed[pygame.K_a]
    vertical =  - pressed[pygame.K_w] + pressed[pygame.K_s]

    if pressed[pygame.K_t]:
        objs.append(object("mushroom", player.image_x, player.image_y))

    if pressed[pygame.K_y]:
        objs.append(object("bottle", player.image_x+10, player.image_y+10))

    player.move(horisontal, vertical)#изменение положения игрока

    #поворот игрока в случае необходимости
    if horisontal < 0:
        player.image_show = player.image_flip
    elif horisontal > 0:
        player.image_show = player.image


    #создание фона
    screen.fill((255, 255, 255))

    #отображение игрока
    screen.blit(player.image_show, (player.image_x, player.image_y))
    for piece in objs:
        screen.blit(piece.image_show, (piece.x, piece.y))


    pygame.display.flip()
    clock.tick(60)