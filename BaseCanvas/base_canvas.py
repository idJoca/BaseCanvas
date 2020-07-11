import pygame
import argparse


class BaseCanvas():
    _continue_flag = True
    BACKGROUND_COLOR = (40, 40, 40)
    FONT_SIZE = 12
    BOLD = False
    ITALIC = False
    SHOULD_FILL = True

    def __init__(self):
        pygame.init()

        self.setup()

        if (self.width == 0 or self.height == 0):
            self.set_fullscreen()
            self.fullscreen = True
        else:
            self.canvas = pygame.display.set_mode(
                (self.width, self.height), pygame.RESIZABLE)
            self.fullscreen = False

        self.screen_size = pygame.Vector2(self.width, self.height)
        self.canvas.fill(self.BACKGROUND_COLOR)
        self.clock = pygame.time.Clock()
        # Use default system font
        self.text_renderer = pygame.font.SysFont(
            pygame.font.get_fonts()[0], self.FONT_SIZE, self.BOLD, self.ITALIC)

        self.init_hook()

    def set_fullscreen(self):
        modes = pygame.display.list_modes()
        biggest_mode = max(modes, key=lambda x: x[0] * x[1])
        self.canvas = pygame.display \
                            .set_mode(
                                biggest_mode,
                                pygame.FULLSCREEN | pygame.SCALED)
        screen_details = self.canvas.get_size()
        self.width = screen_details[0]
        self.height = screen_details[1]

    def setup(self):
        parser = argparse.ArgumentParser(
            description='Pygame Project')
        parser.add_argument('--width', type=int,
                            help='Canvas width', default=800)
        parser.add_argument('--height', type=int,
                            help='Canvas height', default=800)
        parser.add_argument('--fps', type=int,
                            help='Program FPS', default=60)

        self.pre_setup_hook(parser)

        args = parser.parse_args()

        self.width = args.width
        self.height = args.height
        self.fps = args.fps

        try:
            self.setup_hook(args)
        except TypeError as e:
            self.setup_hook()

    def loop(self):
        while self._continue_flag:
            if self.SHOULD_FILL:
                self.canvas.fill(self.BACKGROUND_COLOR)
            self.loop_hook()
            pygame.display.update()
            self._handle_events()
            self.clock.tick(self.fps)

    def _handle_events(self):
        for event in pygame.event.get():
            # Quit the program if the user close the windows
            if event.type == pygame.QUIT:
                pygame.quit()
                self._continue_flag = False
            # Or press ESCAPE
            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    pygame.quit()
                    self._continue_flag = False
                    exit()

                if event.key == pygame.K_F11:
                    if (self.fullscreen is False):
                        self.fullscreen = True
                        pygame.display.quit()
                        pygame.display.init()
                        self.set_fullscreen()
                    else:
                        self.fullscreen = False
                        self.canvas = pygame.display.set_mode((self.width, self.height),
                                                              pygame.RESIZABLE)
                    self.screen_size = pygame.Vector2(self.width, self.height)
                    self.resize_hook()

            if event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.size
                if not self.fullscreen:
                    self.canvas = pygame.display.set_mode((self.width, self.height),
                                                          pygame.RESIZABLE)
                self.screen_size = pygame.Vector2(self.width, self.height)
                self.resize_hook()

            self.handle_events_hook(event)

    def pre_setup_hook(self, parser):
        """
        Here is where any sort of command-line variable declaration should happen.
        This method is called only once.
        This method is intended to be overridden by a heritor.
        """
        pass

    def setup_hook(self, args=None):
        """
        Here is where any sort of variable initialization should happen.
        This method is called only once.
        This method is intended to be overridden by a heritor.
        """
        pass

    def init_hook(self):
        """
        Here is where any sort of pre-loop logic should happen,
        such as, initializing certain classes,
        flow-check (should the program run like this or like that),
        etc.
        This method is called only once.
        This method is intended to be overridden by a heritor.
        """
        pass

    def loop_hook(self):
        """
        Here is we're the application main logic should happen.
        This method is called once every frame.
        This method is intended to be overridden by a heritor.
        """
        pass

    def handle_events_hook(self, event):
        """
        Here is we're the non-default event handling should happen.
        This method is called once every frame.
        This method is intended to be overridden by a heritor.
        """
        pass

    def resize_hook(self):
        """
        This hook will be called when a screen resize happens.
        Use it to take care of screen size dependencies.
        """
        pass
