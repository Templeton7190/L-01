from wpilib import XboxController

from commands import SmoothDrive
from subsystems import Drive


class RobotContainer:
    def __init__(self):
        self.controller = XboxController(0)

        # Subsystems
        self.drive = Drive()
        self.drive.setDefaultCommand(SmoothDrive(self.drive, self.controller))
