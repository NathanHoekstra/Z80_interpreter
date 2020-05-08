import pygame
import numpy as np
from cpu import Cpu


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
        self.icon = pygame.image.load('img/gameboy.png')
        self.finished = False
        self.pixel_count = 16
        self.game_display = pygame.display.set_mode((display_size, display_size))
        pygame.display.set_icon(self.icon)
        self.pixel_size = display_size / self.pixel_count
        self.clock = pygame.time.Clock()
        self.pixel_list = []
        self.__generate_pixel_array()

    def __generate_pixel_array(self):
        for pixel_row in range(self.pixel_count):
            for pixel in range(self.pixel_count):
                self.pixel_list.append(Pixel(pixel * self.pixel_size, pixel_row * self.pixel_size, self.pixel_size))

    @staticmethod
    def get_color(value: np.uint8) -> pygame.color:
        red = (value >> 5) * 255 / 7
        green = ((value >> 2) & 0x07) * 255 / 7
        blue = (value & 0x03) * 255 / 3
        return [red, green, blue]

    def draw(self, cpu: Cpu) -> bool:
        self.game_display.fill((0, 0, 0))
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        # Set pixel values retreived from cpu mem
        for index, pixel in enumerate(self.pixel_list):
            pixel.set_color(self.get_color(cpu.memory[index]))
        # Draw pixels
        for pixel in self.pixel_list:
            pixel.render(self.game_display)
        pygame.display.flip()
