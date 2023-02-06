class DatabaseConnectionException(Exception):
    def __repr__(self):
        return "Database connection error"
