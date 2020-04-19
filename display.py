import pygame

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
BROWN = [153, 102, 17]
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]


class Pixel:
    def __init__(self, position_x, position_y, size):
        self.color = [255, 255, 255]
        self.position_x = position_x
        self.position_y = position_y
        self.size = size

    def set_color(self, color: list):
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.position_x, self.position_y, self.size, self.size))


class Display:
    def __init__(self, display_size: int = 640):
        pygame.init()
        pygame.display.set_caption("Z80 display")
        self.finished = False
        self.pixel_count = 16
        self.game_display = pygame.display.set_mode((display_size, display_size))
        self.pixel_size = display_size / self.pixel_count
        self.clock = pygame.time.Clock()
        self.pixel_list = []
        self.__generate_pixel_array()

    def __generate_pixel_array(self):
        for pixel_row in range(self.pixel_count):
            for pixel in range(self.pixel_count):
                self.pixel_list.append(Pixel(pixel * self.pixel_size, pixel_row * self.pixel_size, self.pixel_size))

    def run(self):
        while not self.finished:
            self.game_display.fill((255, 255, 255))
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
            # Draw pixels
            for pixel in self.pixel_list:
                pixel.render(self.game_display)
            pygame.display.flip()
