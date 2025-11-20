class User:
    """Simple user model."""

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def to_dict(self):
        """Return user as dict."""
        return {"username": self.username, "email": self.email}
