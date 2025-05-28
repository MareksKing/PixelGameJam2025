import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.location_x: float = screen.get_width() / 2
        self.location_y: float = screen.get_height() / 2
        self.height: int = 50
        self.width: int = 100

        self.surface: pygame.Surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(color="blue")
        self.image = self.surface
        self.rect = self.surface.get_rect(center=(self.location_x, self.location_y))
    

class Shadow(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.health: int = 100
        self.x: float = screen.get_width() / 2
        self.y: float = screen.get_height() / 2
        self.speed: int = 10
        self.jump_force: int = 100
        self.gravity: int = 5
        self.on_ground: bool = False

        self.surface: pygame.Surface = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.surface.fill(color="black")
        self.image = self.surface
        self.rect = self.surface.get_rect(center=(self.x, self.y))


    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.on_ground = False
            self.rect.y -= self.jump_force

    def update(self, platforms: list[Platform]):
        self.rect.y += self.gravity
        self.on_ground = False
        if self.rect.collideobjects(platforms):
            self.rect.y -= self.gravity
            self.on_ground = True


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()

    platform = Platform(screen)
    platforms: list[Platform] = []
    platforms.append(platform)
    shadow = Shadow(screen)
    all_sprites.add(platform)
    all_sprites.add(shadow)
    while running:

        screen.fill("purple")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #    platform.draw(screen)
    #    shadow.update(platforms)
        all_sprites.update(platforms)
        all_sprites.draw(screen)
        shadow.handle_keys()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
