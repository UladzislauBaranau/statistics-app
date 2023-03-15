from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from dependencies.usecase_dependencies import get_pages_statistics_management_use_case
from routes.statistics.shema import StatisticsResponse
from use_cases.pages_statistics_management import PagesStatisticsManagementUseCase

router = APIRouter(prefix="/statistics")


@router.get(
    "/pages",
    response_model=StatisticsResponse,
    responses={
        401: {
            "description": "Incorrect User ID",
            "content": {
                "application/json": {
                    "example": {"message": "Incorrect User ID"},
                },
            },
        },
    },
    summary="Get Statistics",
)
async def get_statistics_about_pages(
    pages_statistics_use_case: PagesStatisticsManagementUseCase = Depends(
        get_pages_statistics_management_use_case
    ),
    # get used ID from token using Depends
    user_id: int | None = 1,
) -> Any:
    """
    The endpoint returns statistics about the User's pages and posts.

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

    if not user_id:
        return JSONResponse(status_code=401, content={"message": "Incorrect User ID"})

    pages_statistics = await pages_statistics_use_case.get_statistics(user_id=user_id)
    return pages_statistics
