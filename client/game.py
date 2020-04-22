import pygame


class Game:
    """
    An engine and game manager that manages each game state. When run, the
    current state is updated at a tick rate to process events, update the game
    logic and draw to the screen.
    """

    def __init__(self, surface, states, start_state_name):
        """
        Initialize the Game object.
        ::param surface: the pygame surface
        ::param states: dict mapping of state names to GameState objects
        ::param start_state_name: name of the start state
        """
        self.done = False
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.tick = 60
        self.states = states
        self.current_state_name = start_state_name
        self.current_state = self.states[self.current_state_name]

    def flip_state(self):
        """
        Switch to the next game state.
        """
        current_state_name = self.current_state_name
        next_state_name = self.state.next_state_name
        self.current_state.done = False
        self.current_state_name = next_state_name
        persistent = self.current_state.persistent
        self.current_state = self.states[self.current_state_name]
        self.current_state.startup(persistent)

    def process_events(self):
        """
        Events are passed to the current state for processing.
        """
        for event in pygame.event.get():
            self.current_state.process_event(event)

    def update(self, dt):
        """
        Check for state flip and update the current state.
        :param dt: milliseconds since last tick
        """
        if self.current_state.quit:
            self.done = True
        elif self.current_state.done:
            self.flip_state()

        self.current_state.update(dt)

    def draw(self):
        """
        Draw the current state.
        """
        self.current_state.draw(self.surface)

    def run(self):
        """
        Run the game loop
        """
        while not self.done:
            dt = self.clock.tick(self.tick)
            self.process_events()
            self.update(dt)
            self.draw()
            pygame.display.update()
