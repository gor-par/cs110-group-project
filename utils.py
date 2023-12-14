def get_input(msg):
    """
    A small helper function to return non-enpty terminal inputs

    Args:
    msg (str): message to be displayed in the terminal

    """
    value = input(msg)
    if len(value) == 0:
        print("Error: your input is empty. Please try again")
        return get_input(msg)
    else:
        return value


class ValidationState:
    """
    Small class to make validation easier

    """

    ok = True
    message = None

    def error(self, msg):
        """
        changes status to not OK and stores the message

        args:
        msg (str): the error message
        """
        self.ok = False
        self.message = "Error: " + msg


class InvalidFilenameError(Exception):
    """
    A custom exception for utilizing functions to listen to 
    """

    def __init__(self, message):
        """
        Initialize the custom exception with a given message.
        """
        self.message = message
        super().__init__(self.message)
