import pygame

from client.game_manager import GameManager
from client.game_states.main_menu_state import MainMenuState
from client.game_states.singleplayer_state import SingleplayerState
from client.game_states.player_vs_player_chess_game_state import PlayerVsPlayerChessGameState
from client.game_states.online_multiplayer_state import OnlineMultiplayerState

# Create display surface
surface_size = (750, 750)
pygame.display.set_caption('Online Multiplayer Chess')
surface = pygame.display.set_mode(surface_size)

# Create game states
states = {'MainMenuState': MainMenuState(), 'SingleplayerState': SingleplayerState(),
          'PlayerVsPlayerChessGameState': PlayerVsPlayerChessGameState(), 'OnlineMultiplayerState': OnlineMultiplayerState()}
start_state_name = 'MainMenuState'

# Create the game
game_manager = GameManager(surface, states, start_state_name)
