import pygame

class Cell:
    def __init__(self, position: tuple, size: tuple, color: str, image: str = None) -> None:
        self.position = position
        self.color = color
        self.image = image
        self.size = size
        self.__image_creation()

    def __set_position(self, new_position: tuple) -> None:
        self.position = new_position
    
    def __set_size(self, new_size: tuple) -> None:
        self.size = new_size

    def __image_creation(self) -> None:
        if self.image:
            self.image = pygame.transform.scale(pygame.image.load(self.image), self.size)
            self.rect = self.image.get_rect()
        else:
            raise Exception('При вызове конструктора не была передана картинка в класс')

class Board:
    def __init__(self, window: pygame.Surface, position: tuple) -> None:
        self.position = position
        self.window = window
        self.cells = list()
        self.size = self.__set_size()
        self.__create_cells()

    def __set_size(self) -> tuple:
        '''
        Gets the dimensions of the checkerboard based on the screen size
        '''
        win_width, win_height = self.window.get_size()
        
        margin_x = int(win_width * 0.1)
        margin_y = int(win_height * 0.1)

        adjusted_width = win_width - 2 * margin_x
        adjusted_height = win_height - 2 * margin_y

        symmetric_size = min(adjusted_height, adjusted_width)
        
        return (symmetric_size, symmetric_size)

        

    def __create_cells(self) -> None:
        x, y = self.position
        for row in range(8):
            for col in range(8):
                pass

