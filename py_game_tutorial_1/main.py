import pygame


class App(object):
    def __init__(self):
        self._running = True
        self.background = pygame.image.load('background.png')
        self.hero = pygame.image.load('hero.png')
        self.x = 0
        self.y = 0
        pygame.init()
        self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_event(self, event):
        print(event)
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_UP:
                self.y -= 5
            if event.key == pygame.K_DOWN:
                self.y += 5
            if event.key == pygame.K_RIGHT:
                self.x += 5
            if event.key == pygame.K_LEFT:
                self.x -= 5

    def events(self):
        for event in pygame.event.get():
            self.on_event(event)

    def loop(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def render(self):
        self._display_surf.blit(self.background, (0, 0))
        self._display_surf.blit(self.hero, (self.x, self.y))
        pygame.display.flip()

    def on_execute(self):
        while self._running:
            self.events()
            self.loop()
            self.render()

        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()