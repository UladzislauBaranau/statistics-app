class InvalidUserException(Exception):
    def __repr__(self):
        return "User is not page owner"


class DatabaseConnectionException(Exception):
    def __repr__(self):
        return "Database connection error"
