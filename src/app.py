from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()  # testing


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Statistics service",
        version="0.1.0",
        description="Get statistics about your pages and posts from Innotter application.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
