from typing import Any

from fastapi import APIRouter, Depends, Path

from dependencies.usecases_dependencies import (
    get_current_user,
    get_pages_statistics_management_use_case,
    get_roles_admin_or_moderator,
)
from routes.statistics.schema import StatisticsResponse
from use_cases.pages_statistics_management import PagesStatisticsManagementUseCase

router = APIRouter(prefix="/statistics")


@router.get(
    "/me",
    response_model=list[StatisticsResponse],
    responses={
        403: {
            "description": "Authentication Error",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid authentication credentials"},
                },
            },
        },
    },
    summary="Get statistics for user",
)
async def get_statistics_for_user(
    user_id: int = Depends(get_current_user),
    pages_statistics_use_case: PagesStatisticsManagementUseCase = Depends(
        get_pages_statistics_management_use_case
    ),
) -> Any:
    """
    Expects the **User ID** parameter from a token.

    Response contains next statistics:
    - **pages' information**:
        - id: ID
        - name: name
        - description: description
        - uuid: uuid
        - n_followers: number of followers
        - n_follow_requests: number of follower requests
    - **posts' information**:
        - id: ID
        - n_likes: number of likes
        - page_id: page ID
    """

    pages_statistics = await pages_statistics_use_case.get_statistics(user_id=user_id)
    return pages_statistics


@router.get(
    "/{user_id}",
    response_model=list[StatisticsResponse],
    responses={
        403: {
            "description": "Permission Denied (Current user is not Admin or Moderator)",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Permission denied. Only for admin or moderator"
                    },
                },
            },
        },
        404: {
            "description": "User ID not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Not found"},
                },
            },
        },
    },
    dependencies=[Depends(get_roles_admin_or_moderator)],
    summary="Get statistics for admin/moderator",
)
async def get_statistics_for_admin_or_moderator(
    user_id: int = Path(title="The ID of the user to get", gt=0),
    pages_statistics_use_case: PagesStatisticsManagementUseCase = Depends(
        get_pages_statistics_management_use_case
    ),
) -> Any:
    """
    Expects the **User ID** and **User Role** parameters from a token.

    Response contains the same content as the ***/me*** endpoint.
    """

    pages_statistics = await pages_statistics_use_case.get_statistics(user_id=user_id)
    return pages_statistics
