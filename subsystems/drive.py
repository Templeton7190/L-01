from commands2 import Subsystem  # type: ignore
from rev import CANSparkMax
from wpilib import MotorControllerGroup
from wpilib.drive import DifferentialDrive

Brushed = CANSparkMax.MotorType.kBrushed


class Drive(Subsystem):
    def __init__(self):
        super().__init__()

        left_motor_group = MotorControllerGroup(
            CANSparkMax(1, Brushed), CANSparkMax(2, Brushed)
        )
        right_motor_group = MotorControllerGroup(
            CANSparkMax(3, Brushed), CANSparkMax(4, Brushed)
        )
        self.drive = DifferentialDrive(left_motor_group, right_motor_group)

    def start(self, forward_speed: float, rotation_speed: float) -> None:
        self.drive.arcadeDrive(forward_speed, rotation_speed)

    def stop(self) -> None:
        self.drive.arcadeDrive(0, 0)
