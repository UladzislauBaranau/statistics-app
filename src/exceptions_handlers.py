from fastapi import Request, status
from fastapi.responses import JSONResponse

from core.exceptions import (
    AuthorizationException,
    DatabaseConnectionException,
    PermissionDeniedException,
    StatisticsNotFoundException,
)


async def db_connection_exception_handler(
    request: Request, exc: DatabaseConnectionException
):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": f"{exc.__str__()}"},
    )


async def statistics_exception_handler(
    request: Request, exc: StatisticsNotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"{exc.__str__()}"},
    )


async def permission_exception_handler(
    request: Request, exc: PermissionDeniedException
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"message": f"{exc.__str__()}"},
    )


async def authorization_exception_handler(
    request: Request, exc: AuthorizationException
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"message": f"{exc.__str__()}"},
    )


def include_exceptions_handlers(app):
    app.add_exception_handler(
        DatabaseConnectionException, db_connection_exception_handler
    )
    app.add_exception_handler(StatisticsNotFoundException, statistics_exception_handler)
    app.add_exception_handler(PermissionDeniedException, permission_exception_handler)
    app.add_exception_handler(AuthorizationException, authorization_exception_handler)
