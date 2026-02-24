import pygame
from config import ARM_PORT, DRIVE_PORT, WINDOW_SIZE, WINDOW_TITLE
from core.nxt_controller import NXTController
from input.input_controller import KeyboardController
from ui.window import init_window

def main():
    init_window(WINDOW_SIZE, WINDOW_TITLE)

    robot = NXTController(ARM_PORT, DRIVE_PORT)
    robot.connect()

    keyboard = KeyboardController(robot)

    while keyboard.running:
        for event in pygame.event.get():
            keyboard.handle_event(event)

    robot.close()
    pygame.quit()


if __name__ == "__main__":
    main()
