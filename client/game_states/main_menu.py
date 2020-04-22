import pygame

from client.game_states.game_state import GameState


class MainMenu(GameState):

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
