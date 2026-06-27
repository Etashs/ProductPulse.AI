from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


# -------------------------------
# Request Model
# -------------------------------

class CompareRequest(BaseModel):

    product1_url: str

    product2_url: str


# -------------------------------
# Compare Endpoint
# -------------------------------

@router.post("/compare")
async def compare_products(request: CompareRequest):

    return {

        "status": "success",

        "message": "Backend Connected Successfully",

        "product1_url": request.product1_url,

        "product2_url": request.product2_url

    }