class EnterPressedException(Exception):
    def __init__(self, message="Enter key pressed"):
        super().__init__(message)
