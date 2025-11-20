class Calculator:
    """A simple calculator class."""

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide x by y with zero check."""
        if y == 0:
            return None
        return x / y
