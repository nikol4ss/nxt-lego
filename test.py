import nxt.locator
import nxt.motor
import pygame
import logging

logging.basicConfig(level=logging.DEBUG)

pygame.init()
window = pygame.display.set_mode((100, 100))
pygame.display.set_caption("NXT Keyboard Control")

with nxt.locator.find() as brick:
    arm_motor = brick.get_motor(nxt.motor.Port.A)
    drive_motor = brick.get_motor(nxt.motor.Port.B)

    is_running = True
    is_control_enabled = False

    while is_running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_f:
                    is_control_enabled = True
                    print("Control ENABLED")

                elif event.key == pygame.K_r:
                    is_control_enabled = False
                    print("Control DISABLED")

                elif is_control_enabled:

                    if event.key == pygame.K_DOWN:
                        drive_motor.turn(100, 360)

                    if event.key == pygame.K_UP:
                        drive_motor.turn(-100, 360)

                    if event.key == pygame.K_RIGHT:
                        arm_motor.turn(10, 20)

                    elif event.key == pygame.K_LEFT:
                        arm_motor.turn(-25, 25)
