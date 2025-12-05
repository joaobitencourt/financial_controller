from fastapi import FastAPI
from app.controllers import health_routers as health


app = FastAPI(
    title="finacy controll service",
    description="Lets imagine if you need to storege what you spend during one day and not be confused in the end of the month. That is the service for you and you will be able to create group wiht other persons that will pay one parte of your expenses it will be even better.",
    version="1.0",
    docs_url="/docs", 
    redoc_url="/redoc",
)

app.include_router(health.router)
