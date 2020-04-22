import pygame

from client.game import Game
from client.game_states.singleplayer import Singleplayer

# Create display surface
surface_size = (750, 750)
pygame.display.set_caption('Online Multiplayer Chess')
surface = pygame.display.set_mode(surface_size)

# Create game states
states = {'Singleplayer': Singleplayer()}
start_state_name = 'Singleplayer'

# Create the game
game = Game(surface, states, start_state_name)
