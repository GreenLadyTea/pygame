import pygame


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.w = 25
        self.h = 75
        self.surf = pygame.Surface((self.w, self.h))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def move(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -self.h)
        elif keys[K_LEFT]:
            self.rect.move_ip(-self.w, 0)


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
player = Player()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)

    pygame.display.flip()


pygame.quit()
