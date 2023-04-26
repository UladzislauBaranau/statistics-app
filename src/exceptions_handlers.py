from fastapi import Request, status
from fastapi.responses import JSONResponse

from core.exceptions import (
    AuthorizationException,
    PermissionDeniedException,
    StatisticsNotFoundException,
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
    app.add_exception_handler(StatisticsNotFoundException, statistics_exception_handler)
    app.add_exception_handler(PermissionDeniedException, permission_exception_handler)
    app.add_exception_handler(AuthorizationException, authorization_exception_handler)
