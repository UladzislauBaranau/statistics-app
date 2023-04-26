class DatabaseConnectionException(Exception):
    def __repr__(self):
        return "Database connection error"


class StatisticsNotFoundException(Exception):
    def __str__(self):
        return "Statistics not found"


class AuthorizationException(Exception):
    def __str__(self):
        return "Invalid authentication credentials"


class PermissionDeniedException(Exception):
    def __str__(self):
        return "Permission denied. Only for admin or moderator"
