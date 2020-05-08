import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   # Remove PyGame support prompt
import pygame
import numpy as np
from cpu import Cpu


class Pixel:
    def __init__(self, position_x, position_y, size):
        self.__color = [255, 255, 255]
        self.__position_x = position_x
        self.__position_y = position_y
        self.__size = size

    def set_color(self, color: list):
        self.__color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.__color, (self.__position_x, self.__position_y, self.__size, self.__size))


class Display:
    def __init__(self, display_size: int = 640):
        pygame.init()
        pygame.display.set_caption("Z80 display")
        self.__icon = pygame.image.load('img/gameboy.png')
        self.__finished = False
        self.__pixel_count = 16
        self.__game_display = pygame.display.set_mode((display_size, display_size))
        pygame.display.set_icon(self.__icon)
        self.__pixel_size = display_size / self.__pixel_count
        self.__clock = pygame.time.Clock()
        self.__pixel_list = []
        self.__generate_pixel_array()

    def __generate_pixel_array(self):
        for pixel_row in range(self.__pixel_count):
            for pixel in range(self.__pixel_count):
                self.__pixel_list.append(
                    Pixel(pixel * self.__pixel_size, pixel_row * self.__pixel_size, self.__pixel_size)
                )

    @staticmethod
    def get_color(value: np.uint8) -> pygame.color:
        red = (value >> 5) * 255 / 7
        green = ((value >> 2) & 0x07) * 255 / 7
        blue = (value & 0x03) * 255 / 3
        return [red, green, blue]

    def draw(self, cpu: Cpu) -> bool:
        self.__game_display.fill((0, 0, 0))
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        # Set pixel values retrieved from cpu mem
        for index, pixel in enumerate(self.__pixel_list):
            pixel.set_color(self.get_color(cpu.memory[index]))
        # Draw pixels
        for pixel in self.__pixel_list:
            pixel.render(self.__game_display)
        pygame.display.flip()
