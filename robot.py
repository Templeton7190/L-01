from wpilib import MotorControllerGroup, PWMSparkMax, TimedRobot, XboxController
from wpilib.drive import DifferentialDrive
from wpimath.filter import SlewRateLimiter


class Robot(TimedRobot):
    def robotInit(self) -> None:
        left_motor_group = MotorControllerGroup(PWMSparkMax(1), PWMSparkMax(2))
        right_motor_group = MotorControllerGroup(PWMSparkMax(3), PWMSparkMax(4))
        self.drive = DifferentialDrive(left_motor_group, right_motor_group)
        self.limiter = SlewRateLimiter(0.5)

        self.stick = XboxController(0)

    def teleopPeriodic(self) -> None:
        self.drive.arcadeDrive(
            self.limiter.calculate(self.stick.getLeftY()), self.stick.getRightX()
        )
