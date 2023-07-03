import pygame

class Cell:
    def __init__(self, position: tuple, size: tuple, color: str, image: str = None) -> None:
        self.position = position
        self.size = size
        self.color = color
        self.image = image
        self.__image_creation()

    def __set_position(self, new_position: tuple) -> None:
        self.position = new_position
    
    def __set_size(self, new_size: tuple) -> None:
        self.size = new_size

    def __image_creation(self):
        if self.image:
            self.image = pygame.transform.scale(pygame.image.load(self.image), self.size)
            self.rect = self.image.get_rect()
        else:
            raise Exception('При вызове конструктора не была передана картинка в класс')

class Board:
    pass
