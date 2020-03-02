# BaseCanvas

## Description

BaseCanvas is a small helper-class that handles common tasks in pygame. I've built it because I'm constantly making side-projects, often related to simulations, data structures, little games and stuff and it's not pleasant to always have to paste boilerplate code just to get started. Feel free to contact me, for suggestions, complaints or anything, really.

## Use

To get started simply:

1. Import BaseCanvas

        from base_canvas import BaseCanvas

2. Create a "Main Class" that inherits BaseCanvas

        class Main(BaseCanvas):
            pass

3. Append the following at the end of the file in which your "Main Class" is:

    ```python
    if __name__ == "__main__":
        main = Main()
        main.loop()
    ```

When running your program from the command-line a few parameters can be passed:

- --width (an integer, if 0 fullscreen mode will be selected. Default to 800)
- --height (an integer, if 0 fullscreen mode will be selected. Default to 800)
- --fps (an integer. Default to 60)

## lifecycle

The lifecycle of BaseCanvas is centered around inherited and overwritten hooks. They are 4 in total, each one with there own "responsibilities".

### Setup hook

The setup hook (setup_hook) is the first one to be called, right after **pygame** is initiated. It's intended to do all sort of "variable initialization".
It's **called only once**.

### Init hook

The init hook (init_hook) is the second one to be called. It's intended to do all sort of pre-loop logic,
such as, initializing certain classes, doing a flow-check (should the program run like this or like that), etc. As with the setup hook, it's **called only once**.

### Loop hook

The loop hook (loop_hook) is the third and main hook. It's where all of your main program logic should happen, things like: drawing to the canvas, collision check, etc. It's called at **every frame**, right after filling the main canvas with the "BACKGROUND_COLOR" and before calling "pygame.display.update()".

### Handle events hook

The handle events hook (handle_events_hook) is the fourth and last hook. It's also the only hook that receives an argument, the event itself. It's called at **every frame**. The event (argument) is one element of the list returned by "pygame.event.get()". Keep in mind that some events are "handled" by default. They are:

- pygame.QUIT
- pygame.KEYDOWN
  - pygame.K_ESCAPE
  - pygame.K_F11
- pygame.VIDEORESIZE

## Author

João Pedro Braz, São Paulo - Brazil.

- Email: [brazjoaopedro@ymail.com](brazjoaopedro@ymail.com)
- Linkedin: [João Pedro Braz](https://www.linkedin.com/in/joão-pedro-b-38406b121/)
- Github: [Repositories](https://github.com/idJoca)
