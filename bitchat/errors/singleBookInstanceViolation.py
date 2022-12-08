class SingleBookInstanceViolation(BaseException):
    """
    This Exception is raised when any node of the system
    attempts to create a second Book while there is one of
    them running.
    It ensures that one Book exists by session.
    """
    def __init__(self) -> None:
        super().__init__("Single Book Instance Violation")
