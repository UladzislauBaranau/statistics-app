from app import app
from routes import healthcheck
from routes.statistics import get_page_statistics_router

app.include_router(healthcheck.router, tags=["Healthcheck"])
app.include_router(get_page_statistics_router.router, tags=["Statistics"])
