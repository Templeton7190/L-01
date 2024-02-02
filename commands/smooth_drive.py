from commands2 import Command  # type: ignore
from wpilib import XboxController
from wpimath.filter import SlewRateLimiter

from subsystems import Drive


class SmoothDrive(Command):
    def __init__(self, drive: Drive, controller: XboxController):
        super().__init__()

        self.controller = controller
        self.drive = drive
        self.filter = SlewRateLimiter(0.5)

        self.addRequirements(drive)

    def execute(self) -> None:
        self.drive.start(
            self.filter.calculate(self.controller.getLeftY()),
            self.controller.getRightX(),
        )
