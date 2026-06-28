from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.utils.playstore import fetch_app_data
from app.services.gemini_service import analyze_products

router = APIRouter()


class CompareRequest(BaseModel):
    url1: str
    url2: str


@router.post("/compare")
async def compare(data: CompareRequest):

    try:

        # Fetch Play Store data
        product1 = fetch_app_data(data.url1)
        product2 = fetch_app_data(data.url2)

        # Ask Gemini to analyze both products
        result = analyze_products(product1, product2)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )