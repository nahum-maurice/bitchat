class SingleInstanceViolation(BaseException):
    """
    This Exception is raised when any node of the system
    attempts to create a second instance of a class that is suppose to have
    a single instance.
    It ensures that only one instance exists by session.
    """
    def __init__(self) -> None:
        super().__init__("Single Instance Violation")
