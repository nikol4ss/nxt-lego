import pygame

class KeyboardController:
    def __init__(self, robot):
        self.robot = robot
        self.running = True
        self.control_enabled = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.KEYDOWN:
            self._handle_keydown(event.key)

    def _handle_keydown(self, key):

        if key == pygame.K_f:
            self.control_enabled = True
            print("Control ENABLED")
            return

        if key == pygame.K_r:
            self.control_enabled = False
            print("Control DISABLED")
            return

        if not self.control_enabled:
            return

        if key == pygame.K_DOWN:
            self.robot.drive_backward()

        elif key == pygame.K_UP:
            self.robot.drive_forward()

        elif key == pygame.K_RIGHT:
            self.robot.arm_right()

        elif key == pygame.K_LEFT:
            self.robot.arm_left()
