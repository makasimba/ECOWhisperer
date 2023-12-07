class MisuseException(Exception):
    """Exception raised for inappropriate user input."""

    def __init__(self, message):
        super().__init__(self.message)
        self.message = message

    def __str__(self):
        return self.message
