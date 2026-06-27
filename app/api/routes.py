from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "Backend running successfully"
    }


@router.post("/compare")
async def compare():
    return {
        "status": "success",
        "message": "Compare API working",
        "data": {}
    }
