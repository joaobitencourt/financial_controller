from fastapi import APIRouter

#configs da rota
router = APIRouter(
    prefix="/api/v1/fpc",
    tags=["health"]
)

@router.get("/")
def health_check():
    return {
        "status": "OK",
        "service": "Financy Control API",
        "version": "1.0.0"
    }

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/info")
def service_info():
    return {
        "name": "Financy Control Service",
        "description": "Expense tracking and cost sharing",
        "status": "operational"
    }