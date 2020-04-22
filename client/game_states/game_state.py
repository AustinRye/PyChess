class GameState:

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state_name = None
        self.persist = None

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        :param persistent: dict passed from previous state
        """
        self.persist = persistent

    def process_event(self, event):
        """
        Process a single pygame event.
        """
        pass

    def update(self, dt):
        """
        Update the game state.
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen's surface.
        """
        pass
