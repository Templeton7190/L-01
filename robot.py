from commands2 import TimedCommandRobot  # type: ignore

from robot_container import RobotContainer


class Robot(TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()
