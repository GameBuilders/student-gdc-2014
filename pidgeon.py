import pygame

# Pidgeon class. Stores pidgeon attack and rendering information.
class Pidgeon():
    # Constructor. Loads pidgeon assets
    def __init__(self, type):
        if (type == 0):
            self.sprite = pygame.image.load(os.path.join('assets', 'pidgeon.png'))
    
    # Render the pidgeon
    def render(self, position):
        screen = pygame.display.get_surface()
        screen.blit(self.sprite, position)
