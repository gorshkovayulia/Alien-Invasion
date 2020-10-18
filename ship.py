import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initiates a ship and set its start position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Each new ship appears at the bottom of screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Saving a float coordinate of ship center.
        self.center = float(self.rect.centerx)

        # Flag of moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the position of ship depending on flags."""
        # Updates the center attribute, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updating the rect attribute based on self.center.
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
