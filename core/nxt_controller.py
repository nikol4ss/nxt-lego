import nxt.locator

class NXTController:
    def __init__(self, arm_port, drive_port):
        self.brick = None
        self.arm_port = arm_port
        self.drive_port = drive_port
        self.arm_motor = None
        self.drive_motor = None

    def connect(self):
        self.brick = nxt.locator.find()
        self.arm_motor = self.brick.get_motor(self.arm_port)
        self.drive_motor = self.brick.get_motor(self.drive_port)

    def drive_forward(self):
        self.drive_motor.turn(-100, 360) # pyright: ignore[reportOptionalMemberAccess]

    def drive_backward(self):
        self.drive_motor.turn(100, 360) # pyright: ignore[reportOptionalMemberAccess]

    def arm_right(self):
        self.arm_motor.turn(10, 20) # pyright: ignore[reportOptionalMemberAccess]

    def arm_left(self):
        self.arm_motor.turn(-25, 25) # pyright: ignore[reportOptionalMemberAccess]

    def close(self):
        if self.brick:
            self.brick.close()
