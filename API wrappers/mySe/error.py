class MySE(Exception):
    """Base exception catcher."""
    pass


class UnauthorizedError(MySE):
    """Exception that occurs when an invalid token/email has been given."""
    pass
